# Linux Bootstrap Script

A Python script to set up a fresh Ubuntu dev box with common tools, or safely
re-check an already-configured one.

## What it does

1. Updates the system's package list and upgrades installed packages
2. Installs common dev tools: `git`, `curl`, `build-essential`, `python3-pip`, `vim`, `htop`, `unzip`
3. Installs GitHub CLI (`gh`) if it isn't already present
4. Checks for an SSH key (`~/.ssh/id_ed25519`) — does not auto-generate one, to avoid overwriting an existing key
5. Checks your git identity (`user.name` / `user.email`) and prompts for it if missing

Every step checks whether it's already done before acting, so it's safe to
run more than once on the same machine.

## Usage

```bash
python3 bootstrap.py
```

## Requirements

- Ubuntu (tested on 22.04)
- `sudo` privileges
- Python 3

## Notes

- Does not generate an SSH key automatically — if one is missing, the script
  will tell you the command to run yourself.
- If git identity isn't set, it will prompt for your name and email
  interactively during the run.
