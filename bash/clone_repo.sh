#!/bin/bash

getModuleAlias()
{
    ALIAS=()
    ISNUM='^[0-9]+$'
    
    for IT in ${ARRAY[@]}
    do
	ISINARRAY=0
	TMP=$(echo $IT | cut -d _ -f 1)
	for NEW in ${ALIAS[@]}
	do
	    if [ "$NEW" = "${TMP^^}" ]
	    then
		ISINARRAY=1
		break
	    fi
	    if [[ "${TMP:0:1}" =~ $ISNUM ]]
	    then
		ISINARRAY=1
		break
	    fi
	    
	done
	if [ "${#ALIAS[@]}" = 0 -o $ISINARRAY = 0 ]
	then
	    ALIAS+=(${TMP^^})
	fi
    done
    displayList $ALIAS $ARRAY
}

displayList()
{
    ALIAS+=("OTHERS")
    
    for IT in ${ALIAS[@]}
    do
	LINE=0
	echo -e "\e[92m[\e[31m $IT \e[92m] ---\e[39m"
	for DISP in ${ARRAY[@]}
	do
	    if [[ "${DISP[@]}" == *"${IT[@]}"* ]]
	    then
		echo -n $DISP " "
		LINE+=1
		if [ "$LINE" = 5 ]
		then
		    echo
		    LINE=0
		fi
	    fi
	done
	echo
    done
}

# Getting all repositories from an user
getRepoList()
{
    LIST=""

    LIST=$(blih -u $USER@epitech.eu repository list | sort)
    ARRAY=($LIST)
    if [ ${ARRAY[0]} = "Error" ]
    then
	echo "Error message : Bad token"
	getRepoList USER
    else
	getModuleAlias $ARRAY
    fi
}

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
