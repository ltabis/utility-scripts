#!/bin/bash

blih -u lucas.tabis@epitech.eu repository create $1
blih -u lucas.tabis@epitech.eu repository setacl $1 ramassage-tek r
git clone git@git.epitech.eu:/lucas.tabis@epitech.eu/$1
