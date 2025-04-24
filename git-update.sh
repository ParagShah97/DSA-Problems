#!/bin/bash

# Bash script to automate Git add, commit, pull, and push

# Prompt for commit message
read -p "Enter commit message: " commit_msg

# Git commands
git add .
git commit -m "$commit_msg"
git pull origin main
git push origin main