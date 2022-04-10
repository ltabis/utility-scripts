#!/usr/bin/env python3

import configparser
import sys
import os

help = """
HOW TO USE:\n
    ./commit.py type title description\n
    -- types [Keyword -> meaning]
    \nCode:
       . up     ->  general update of the code
       . feat   ->  new feature
       . fact   ->  refactoring the code
       . perf   ->  performance improvement
       . struct ->  structure of the code
    \nFixes:
       . fix    ->  quick fix of the code
       . bug    ->  bug fix
       . sec    ->  security fix
       . lint   ->  removing linter warnings and errors
    \nProject:
       . ci     ->  Updating/Adding CI build system
       . depa   ->  Adding a dependency.
       . depd   ->  Removing a dependency.
       . conf   ->  Changing configuration files.
       . rm     ->  removing file(s) / code
       . mv     ->  Moving or renaming files.
    \nOther:
       . doc    ->  documentation
       . test   ->  unit testing
       . merge  ->  merging branches
       . wip    ->  work in progress
       . new    ->  Experimenting new things
"""

config = configparser.ConfigParser()
config.read_file(open("/etc/emojis.conf"))

print(help)

type = input("\nType of the commit > ")
tp = config['emojis'].get(type)

if tp != None:
    os.system("git commit -m \":" + tp + ": \"")
    os.system("git commit --amend")
else:
    print("Error: the type of your commit doesn't exist.", file=sys.stderr)
    print(help)
    exit(1)
