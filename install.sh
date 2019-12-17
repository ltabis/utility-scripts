#!/bin/bash

echo "o------------------------------------------------------o"
echo "| Welcome to the utility scripts installation software |"
echo "|                Created by Tabis L.                   |"
echo "o------------------------------------------------------o"
echo
echo "This software will install the following programs :"
echo -e "> \e[32mclean\e[0m: Cleans temporary files."
echo -e "> \e[32mclone_repo.sh\e[0m: Clone an Epitech repository."
echo -e "> \e[32mcommit.py\e[0m: Commit to a repository."
echo -e "> \e[32mcreate_repo.sh\e[0m: Create a github repository."
echo -e "> \e[32mprepare_my_repo.sh\e[0m: Create an Epitech repository."
echo -e "> \e[32mpush_that.sh\e[0m: Push to a given branch."
echo -e "> \e[32mrm_docker_images.sh\e[0m: delete all of your docker images."
echo -e "> \e[32m(WIP) update.sh\e[0m: Update the packages installed on your computer -> only works for apt."
echo -e "> \e[32mtrash.py\e[0m: empty trash from the command line."
echo -e "> \e[32m(WIP) integration.py\e[0m: checks your unit tests and push them on a branch if they succeeded."

echo -e "\n"
read -ep "Do you want to install them all ? Yes, there isn't any options to choose wich to install ;) (Y//N) " IN

if [ "$IN" != "Y" ] && [ "$IN" != "y" ]
then
    exit 0
fi

echo -e "\nCopying config files into /etc ..."
cp config/bindings.conf config/emoji.conf config/pipeline.conf /etc

echo -e "Creating executables ..."
chmod 755 bash/clean
chmod 755 bash/clone_repo.sh
chmod 755 bash/create_repo.sh
chmod 755 bash/prepare_my_repo.sh
chmod 755 bash/rm_docker_images.sh
chmod 755 bash/update.sh

chmod 755 python3/integration.py
chmod 755 python3/commit.py
chmod 755 python3/trash.py

echo -e "Copying scripts into /usr/bin ..."
cp bash/clean bash/clone_repo.sh python3/integration.py python3/trash.py python3/commit.py python3/confReader.py bash/create_repo.sh bash/prepare_my_repo.sh bash/rm_docker_images.sh bash/update.sh /usr/bin
echo -e "\nall done!"