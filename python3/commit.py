#!/usr/bin/env python3

from confReader import *
import sys
import os

def display_help():
    print("HOW TO USE:\n")
    print("./commit.py type title description\n")
    print("-- types [Keyword -> meaning]")

    print("\nCode:")
    print("   . feat   ->  new feature")
    print("   . fact   ->  refactoring the code")
    print("   . perf   ->  performance improvement")
    print("   . struct ->  structure of the code")

    print("\nFixes:")
    print("   . up     ->  general update of the code")
    print("   . fix    ->  quick fix of the code")
    print("   . bug    ->  bug fix")

    print("\nOther:")
    print("   . rm     ->  removing file(s) / code")
    print("   . doc    ->  documentation")
    print("   . test   ->  unit testing")
    print("   . merge  ->  merging branches")

rEmoji = ConfigReader("/etc/emoji.conf")

display_help()
type = input("\nType of the commit > ")
description = input("description of the commit > ")

tp = rEmoji.get(type)

if tp != None:
    os.system("git commit -m \"" + tp + " " + description + "\"")
else:
    print("Error: the type of your commit doesn't exist.", file=sys.stderr)
    display_help()
    exit(1)
