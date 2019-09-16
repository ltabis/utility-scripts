#!/bin/bash

read -p "Epitech repository to clone : " repo
read -p "Epitech user to clone from : " user

git clone git@git.epitech.eu:/$user@epitech.eu/$repo
