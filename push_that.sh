#!/bin/bash

read -p "Message de mise à jour : " message

git add --all
git commit -m "$message"
git push --force
