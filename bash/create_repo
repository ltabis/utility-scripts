#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Error : retry with ./create_repo repo_name"
    exit 1
fi

mkdir $1
cd $1

git init
touch README.md
git add README.md
git commit -m "Initial commit."
