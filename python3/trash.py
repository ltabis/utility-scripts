#!/usr/bin/env python3

import os

# Search trash files
path = os.path.join(os.path.expanduser("~/") + ".local/share/Trash/files")
files = os.listdir(path)

if len(files) == 0:
    print("There isn't any file to discard.")
    exit(0)
res = input("There are/is " + str(len(files)) + " file(s) in the trash. Would you like to discard them ? (Y\\N)  ")

# Ask user for input
if res == "Y" or res == "y":
    print("files deleted: ")
    [print("-> " + file) for file in files]
    os.system("rm -r ~/.local/share/Trash/files/*")
else:
    print("current files are: ")
    [print("-> " + file) for file in files]
