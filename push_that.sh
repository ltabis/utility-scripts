#!/bin/bash

read -p "Commit message : " message
read -p "Branch : " branch

git add --all
git commit -m "$message"
git push origin $branch

read -p "All changes were pushed successfully to origin/$branch"
