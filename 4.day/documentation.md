# 🐾 Dawgs Merge Project — Documentation & Runbook

> A complete guide to the Git branching and merging workflow practiced in the `dawgs_marge_test` project.

---

## 📖 What Is This Project?

This project is a hands-on practice run for learning **Git branching and merging** — one of the most important skills in collaborative software development.

> **Analogy:** Think of Git like a school notebook. The `main` branch is your final, clean copy. When you want to try something new, you don't scribble directly in the final copy — you grab a fresh sheet of paper (a **branch**), do your work there, and *then* copy it into the final notebook (a **merge**).

---

## 🗂️ Project Info

| Field | Value |
|---|---|
| **Repository Name** | `dawgs_marge_test` |
| **GitHub Owner** | `Jae1-alt` |
| **Clone URL** | `https://github.com/Jae1-alt/dawgs_marge_test.git` |
| **Base Branch** | `main` |

---

## 🚀 Step-by-Step Runbook

### Step 1 — Clone the Repository

```bash
git clone https://github.com/Jae1-alt/dawgs_marge_test.git
```

> **What this does:** Downloads the entire project from GitHub onto your computer. Like photocopying a textbook so you have your own copy to work from.

---

### Step 2 — Navigate Into the Project

```bash
cd dawgs_marge_test/
```

> **What this does:** Moves you inside the project folder. You must be inside the folder for Git commands to work — Git looks for a hidden `.git` folder here. If you're not inside, you'll get a `fatal: not a git repository` error.

---

### Step 3 — Create and Switch to a New Branch

```bash
git checkout -b <branch-name>
```

> **What this does:** Creates a brand-new branch *and* immediately switches to it. Like tearing off a fresh sheet from a notepad to do your work on, without touching the original.

**Example:**
```bash
git checkout -b feature/day4-files
```

---

### Step 4 — Create a Directory and a File

```bash
mkdir 4.day && cd 4.day
touch file.txt
```

> **What this does:** `mkdir` creates a new folder called `4.day`. `touch` creates an empty file inside it. The `&&` means "do the second command only if the first one works."

---

### Step 5 — Track the New Branch on GitHub

```bash
git push -u origin <branch-name>
```

> **What this does:** Sends your new branch up to GitHub and sets up a connection (tracking) between your local branch and the remote one. The `-u` flag is like telling your branch, "this is your home on GitHub — remember it."

---

### Step 6 — Stage, Commit, and Push Changes

```bash
git add .
git commit -m "test"
git push -u origin <branch-name>
```

> **What each command does:**
> - `git add .` — Packs up all your changed files, ready to save. Like putting papers into an envelope.
> - `git commit -m "test"` — Saves a snapshot with a label. Like sealing the envelope and writing a note on the outside.
> - `git push` — Sends the snapshot up to GitHub. Like mailing the envelope.

---

### Step 7 — Merge the Branch Into `main`

#### Option A: Merge via GitHub (Pull Request button) ✅ Recommended

Use the **"Merge pull request"** button on GitHub for a clean, reviewed merge.

#### Option B: Manual Merge from the Command Line

```bash
git pull origin main       # Get the latest version of main
git checkout main          # Switch to the main branch
git merge <branch-name>    # Merge your branch into main
git push -u origin main    # Push the updated main to GitHub
```

> **What this does:** You're switching back to your "final notebook" (`main`), copying in all your work from the scratch paper (your branch), and then saving the updated final notebook back to GitHub.

---

## 🌿 Branch Management Cheat Sheet

| Command | What It Does |
|---|---|
| `git branch` | List all local branches |
| `git branch <name>` | Create a new branch (doesn't switch to it) |
| `git branch -m <new-name>` | Rename the current branch |
| `git branch -d <name>` | Delete a branch (safe — won't delete if unmerged) |
| `git switch <name>` | Switch to a different branch |
| `git merge <name>` | Merge the named branch into your current branch |

---

## ⚠️ Common Mistakes & Fixes

| Problem | Cause | Fix |
|---|---|---|
| `fatal: not a git repository` | You're not inside the project folder | Run `ls -a` to check for `.git`, then `cd` into the right folder |
| `push` rejected | Remote has changes you don't have | Run `git pull origin main` first, then push |
| Forgot to create a branch | Made changes directly on `main` | Create a branch now: `git checkout -b <name>`, your changes come with you |
| Merge conflict | Two branches changed the same line | Open the conflicted file, resolve the `<<<` / `>>>` markers, then `git add` and `git commit` |

---

## 🔁 Full Workflow at a Glance

```
Clone repo
    │
    ▼
cd into repo
    │
    ▼
git checkout -b <branch>     ← create your scratch paper
    │
    ▼
mkdir / touch / edit files
    │
    ▼
git add . → git commit → git push
    │
    ▼
Open Pull Request on GitHub  ← or merge manually
    │
    ▼
git checkout main → git merge <branch> → git push
```

---

## 📚 Key Concepts Glossary

| Term | Simple Explanation |
|---|---|
| **Repository (repo)** | The project folder that Git is tracking |
| **Branch** | A parallel copy of the project where you can work safely |
| **Commit** | A saved snapshot of your changes at a moment in time |
| **Push** | Upload your local commits to GitHub |
| **Pull** | Download the latest changes from GitHub to your machine |
| **Merge** | Combine the work from one branch into another |
| **Origin** | The default nickname for your GitHub remote |
| **Main** | The primary, production-ready branch of the project |

---

*Runbook generated for the `dawgs-merge-project` · Last updated: May 2026*