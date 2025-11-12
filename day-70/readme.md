# Day 70 – Advanced – Git, GitHub & Version Control

## 🎯 Objective  
Today I deep-dived into advanced features of version control using Git and collaborative workflows with GitHub.  
As I continue to build my cloud-native, AI-enabled software development skills, mastering Git and GitHub is essential for versioning, collaboration, code quality and CI/CD readiness.

## ✅ What I Learned  
- Why version control matters: tracking changes, collaborating effectively, reverting mistakes and managing branching. :contentReference[oaicite:2]{index=2}  
- The workflow of Git: initialize a repository (`git init`), stage changes (`git add`), commit (`git commit`), inspect history (`git log`). :contentReference[oaicite:3]{index=3}  
- Branching and merging: creating (`git branch`, `git checkout -b`), switching branches (`git checkout`), merging changes back and handling merge conflicts. :contentReference[oaicite:4]{index=4}  
- Remote collaboration via GitHub: pushing local work to a remote repo (`git push`), pulling changes (`git pull`), collaborating via branches and pull requests on GitHub. :contentReference[oaicite:5]{index=5}  
- Advanced Git features (at a glance): using `git stash` to temporarily save changes, rebasing vs merging, tags for versioning, and making use of the reflog (`git reflog`). :contentReference[oaicite:6]{index=6}  
- Best practices: commit often with meaningful messages, keep branches focused, sync frequently, resolve conflicts mindfully, and maintain a clean history.  

## 🧪 Hands-On Practice  
- Set up a new Git repository for a small sample project.  
- Created a `main` branch and then a feature branch (e.g., `Chapter 1`).  
- Made code changes, staged and committed them with descriptive messages.  
- Pushed branch to GitHub, opened a pull request, reviewed changes, merged back into `main`.  
- Introduced a deliberate merge conflict (edited the same line in different branches), practiced resolving it.  
- Experimented with `git stash` to set aside unfinished work, then reapplied it.  
- Tagged a commit (e.g., `v1.0.0`) to mark a release candidate.  
- Used GitHub’s remote history view to examine commit graphs and branch merges.

## 📘 Key Commands Summary  
```bash
# Start a repository  
git init  

# Stage files & commit  
git add <file(s)>  
git commit -m "Meaningful commit message"  

# Branching  
git branch <name>  
git checkout <name>  
# or in one line  
git checkout -b <feature-branch>  

# Merging  
git checkout main  
git merge <feature-branch>  

# Handling remote  
git remote add origin <url>  
git push -u origin main  
git pull  

# Advanced  
git stash  
git reflog  
git tag v1.0.0  
git rebase <branch>  
