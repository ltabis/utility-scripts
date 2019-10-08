#!/bin/bash

doCommit()
{
    # git commit -m "\e[92m[\e[91m$TYPE\e[92m] \e[33m$TITL \e[39m: \e[34m$COMMIT\e[39m["
    git commit -m "[$TYPE] $TITLE : $COMMIT"
}


read -p "Type of the commit (fix/feat/minor/merge): " TYPE
read -p "Title of the commit : " TITLE
read -p "Message of the commit : " COMMIT

for IT in 'fix' 'feat' 'minor' 'merge'
do
    if [ "$TYPE" = "$IT" ]
    then
	doCommit $TYPE $TITLE $COMMIT
    fi
done
