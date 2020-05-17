#!/usr/bin/env python3

from confReader import *
import sys
import os

def display_help():
    print("HOW TO USE:\n")
    print("./commit.py type title description\n")
    print("-- types [Keyword -> meaning]")

    print("\nCode:")
    print("   . up     ->  general update of the code")
    print("   . feat   ->  new feature")
    print("   . fact   ->  refactoring the code")
    print("   . perf   ->  performance improvement")
    print("   . struct ->  structure of the code")
    
    print("\nFixes:")
    print("   . fix    ->  quick fix of the code")
    print("   . bug    ->  bug fix")
    print("   . sec    ->  security fix")
    print("   . lint   ->  removing linter warnings and errors")

    print("\nProject:")
    print("   . ci     ->  Updating/Adding CI build system")
    print("   . depa   ->  Adding a dependency.")
    print("   . depd   ->  Removing a dependency.")
    print("   . conf   ->  Changing configuration files.")
    print("   . rm     ->  removing file(s) / code")
    print("   . mv     ->  Moving or renaming files.")

    print("\nOther:")
    print("   . doc    ->  documentation")
    print("   . test   ->  unit testing")
    print("   . merge  ->  merging branches")
    print("   . wip    ->  work in progress")
    print("   . new    ->  Experimenting new things")

rEmoji = ConfigReader("/etc/emoji.conf")

display_help()
type = input("\nType of the commit > ")

tp = rEmoji.get(type)

if tp != None:
    os.system("git commit -m \"" + tp + " \"")
    os.system("git commit --amend")
else:
    print("Error: the type of your commit doesn't exist.", file=sys.stderr)
    display_help()
    exit(1)
