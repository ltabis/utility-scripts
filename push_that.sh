#!/bin/bash

read -p "Commit message : " message

git add --all
git commit -m "$message"
git push --force

read -p "All changes were pushed successfully !"
