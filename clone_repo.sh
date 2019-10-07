#!/bin/bash

# Getting all repositories from an user
getRepoList()
{
    LIST=""

    LIST=$(blih -u $USER@epitech.eu repository list | sort) #| tr '\n' ' '
    ARRAY=($LIST)
    echo ${ARRAY[@]}
    # getModuleAlias $ARRAY
}

# getModuleAlias()
# {
#     for it in ${ARRAY[@]}
#     do
	
#     done
# }

cloneRepository()
{
    read -p "Epitech repository to clone : " REPO
    git clone git@git.epitech.eu:/$0@epitech.eu/$REPO
}

getBlihUser()
{
    read -p "Epitech user to clone from : " USER

    if [ "$1" = "-l" -o "$1" = "--list" ]
    then
	getRepoList USER
    fi
    cloneRepository $1
}


getBlihUser $1
