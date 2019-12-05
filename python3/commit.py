#!/usr/bin/env python3

from confReader import *
import sys
import os

def display_help():
    print("HOW TO USE:\n")
    print("./commit.py type title description\n")
    print("-- types [Keyword -> meaning]")
    print("   . struct ->  structure of the code")
    print("   . perf   ->  performance improvement")
    print("   . rm     ->  removing file(s) / code")
    print("   . bug    ->  bug fix")
    print("   . feat   ->  new feature")
    print("   . doc    ->  documentation")
    print("   . test   ->  unit testing")
    print("   . merge  ->  merging branches")
    print("   . fact   ->  refactoring the code")

rEmoji = ConfigReader("/etc/emoji.conf")
rBindings = ConfigReader("/etc/bindings.conf")

display_help()
type = input("Type of the commit > ")
title = input("title of the commit > ")
description = input("description of the commit > ")


if type != None:
    os.system("git commit -m \"{" + str(rEmoji.get(type)) + " " + str(rBindings.get(type)) + "} " + title + " : " + description + "\"")
else:
    print("Error: the type of your commit doesn't exist.", file=sys.stderr)
    display_help()
    exit(1)
