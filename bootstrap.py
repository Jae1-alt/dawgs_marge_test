#!/usr/bin/env python3
"""
Bootstrap script for a fresh (or existing) Ubuntu dev box.
Safe to re-run - every step checks "is this already done?" before acting,
kind of like a checklist where you tick off what's already finished
instead of redoing everything from scratch.
"""

import subprocess
import shutil
import os

def run(cmd, description):
    """
    Runs a shell command and prints what it's doing.
    'cmd' is a list of words, e.g. ["sudo", "apt", "update"]
    - this is safer than one long string because it avoids weird
    quoting/spacing bugs.
    """
    print(f"-> {description}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"   WARNING: {description} had an issue:\n{result.stderr.strip()}")
    return result

def update_system():
    print("\n=== Updating package lists and upgrading system ===")
    run(["sudo", "apt", "update"], "refreshing package catalog")
    run(["sudo", "apt", "upgrade", "-y"], "upgrading installed packages")

def install_packages():
    """
    Installs a list of common dev tools, but only the ones not
    already installed - checked via dpkg (Ubuntu's package tracker).
    """
    print("\n=== Installing common dev packages ===")
    packages = ["git", "curl", "build-essential", "python3-pip", "vim", "htop", "unzip"]

    for pkg in packages:
        check = subprocess.run(["dpkg", "-s", pkg], capture_output=True)
        if check.returncode == 0:
            print(f"-> {pkg} already installed, skipping")
        else:
            run(["sudo", "apt", "install", "-y", pkg], f"installing {pkg}")

def install_gh_cli():
    """
    shutil.which() is like asking 'does the system know where this
    program lives?' - if it returns a path, it's already installed.
    """
    print("\n=== Checking for GitHub CLI (gh) ===")
    if shutil.which("gh"):
        print("-> gh already installed, skipping")
        return

    print("-> gh not found, installing...")
    commands = [
        (["bash", "-c",
          "curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg "
          "| sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg"],
         "adding GitHub's signing key"),
        (["sudo", "chmod", "go+r", "/usr/share/keyrings/githubcli-archive-keyring.gpg"],
         "fixing key permissions"),
        (["bash", "-c",
          'echo "deb [arch=$(dpkg --print-architecture) '
          'signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] '
          'https://cli.github.com/packages stable main" '
          '| sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null'],
         "adding gh's package source"),
        (["sudo", "apt", "update"], "refreshing package catalog"),
        (["sudo", "apt", "install", "-y", "gh"], "installing gh"),
    ]
    for cmd, desc in commands:
        run(cmd, desc)

def check_ssh_key():
    """
    Just checks - does NOT generate one automatically, since overwriting
    an existing key by accident could break access to things.
    """
    print("\n=== Checking for SSH key ===")
    key_path = os.path.expanduser("~/.ssh/id_ed25519")
    if os.path.exists(key_path):
        print(f"-> SSH key already exists at {key_path}")
    else:
        print(f"-> No SSH key found at {key_path}")
        print("   Run: ssh-keygen -t ed25519 -C \"your_email@example.com\"")

def check_git_identity():
    """
    Checks if git already knows who you are, and only prompts
    if it doesn't - so it won't overwrite an identity you already set.
    """
    print("\n=== Checking git identity ===")
    name = subprocess.run(["git", "config", "--global", "user.name"],
                           capture_output=True, text=True).stdout.strip()
    email = subprocess.run(["git", "config", "--global", "user.email"],
                            capture_output=True, text=True).stdout.strip()

    if name and email:
        print(f"-> git identity already set: {name} <{email}>")
    else:
        print("-> git identity not fully set.")
        new_name = input("   Enter your name for git commits: ").strip()
        new_email = input("   Enter your email for git commits: ").strip()
        subprocess.run(["git", "config", "--global", "user.name", new_name])
        subprocess.run(["git", "config", "--global", "user.email", new_email])
        print("-> git identity saved.")

def main():
    print("=== Starting bootstrap ===")
    update_system()
    install_packages()
    install_gh_cli()
    check_ssh_key()
    check_git_identity()
    print("\n=== Bootstrap complete ===")

if __name__ == "__main__":
    main()
