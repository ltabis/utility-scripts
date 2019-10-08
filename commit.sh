#!/bin/bash

doCommit()
{
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
