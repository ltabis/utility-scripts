#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Error : retry with ./prepare_my_repo.sh email repo_name"
fi

blih -u $1 repository create $2
blih -u $1 repository setacl $2 ramassage-tek r

git clone git@git.epitech.eu:/$1/$2

cd $2
