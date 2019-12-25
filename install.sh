#!/bin/bash

# using whiptail as the UI
RESULTS=$(whiptail --title "Install Software" --checklist \
"                                              o------------------------------------------------------o
                                              | Welcome to the utility scripts installation software |
                                              |                Created by Tabis L.                   |
                                              o------------------------------------------------------o
                                                            Select wich programs to install" 20 150 10 \
"clean" "Cleans temporary files." OFF \
"clone_repo" "Clone an Epitech repository." OFF \
"commit" "Special format commits." OFF \
"create_repo" "Create a github repository." OFF \
"prepare_my_repo" "Create an Epitech repository." OFF \
"rm_docker_images" "Delete all of your docker images." OFF \
"update" "(WIP) Update the packages installed on your computer -> only works for apt." OFF \
"trash" "empty trash from the command line." OFF \
"integration" "(WIP) checks your unit tests and push them on a branch if they succeeded." OFF 3>&1 1>&2 2>&3)

# Scripts paths
SCRIPTS=(bash/clean bash/clone_repo.sh python3/commit.py bash/create_repo.sh bash/prepare_my_repo.sh bash/rm_docker_images.sh bash/update.sh python3/trash.py python3/integration.py)
NAMES=("clean" "clone_repo" "commit" "create_repo" "prepare_my_repo" "rm_docker_images" "update" "trash" "integration")
TOINSTALL=()

# Get the appropriate programs
for SELECTED in ${RESULTS[@]}
do
    for i in ${!NAMES[@]}
    do
       if [[ "$SELECTED" == *"${NAMES[$i]}"* ]]
        then
            TOINSTALL=("${TOINSTALL[@]}" ${SCRIPTS[$i]})
        fi
    done
done

# Check if programs have been selected
if [ ${#TOINSTALL[@]} -eq 0 ]
then
    echo "Nothing selected for installation, stopping ..."
    exit 0
fi

# Copying config files
echo -e "\nCopying config files into /etc ...\n"
cp config/emoji.conf config/configpath.conf /etc

# Copying python dependancies
cp python3/confReader.py /usr/bin/

# chmod + installation of scripts
for PROGRAM in ${TOINSTALL[@]}
do
    echo -e "Copying $PROGRAM into /usr/bin ..."
    chmod 755 $PROGRAM
    cp $PROGRAM /usr/bin
done

echo -e "\nall done!"
