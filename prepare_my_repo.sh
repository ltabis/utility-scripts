#!/bin/bash

blih -u $1 repository create $2
blih -u $1 repository setacl $2 ramassage-tek r

git clone git@git.epitech.eu:/$1/$2
cd $2
cp ~/utils/.gitignore .
git add .gitignore
git commit -m "Initial commit."
git push origin master

