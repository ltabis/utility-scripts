#!/usr/bin/env python

import os
import sys
import subprocess

sourcetype = "cpp"
objecttype = "o"

configfilepath = ".config"

sourcedirectory = ""
objectdirectory = ""
compilationcommand = ""

###################
### Object file ###
###################

# Display changes in sources.
def show_changes():
    pass

# Execute the compilation command to reload object files.
def execute_command(commandline):

    # Executing command.
    process = subprocess.Popen(commandline, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Run while the command didn't end.
    while True:
        
        # Reading return code.
        output = process.stderr.readline()
        if len(output):
            print(f"error: {output.strip()}")
        returncode = process.poll()

        # Process has finished        
        if returncode is not None:
            if returncode:
                print(f"return code: {returncode}")
            for output in process.stdout.readlines():
                print(f"output: {output.strip()}")
            break

# Exclude files that aren't the same type that the extension passed as parameter
def exclude_files(files, extension):

    return [file for file in files if file.split('.')[-1] == extension]

# Getting files by directory and types
def get_files(directory, type):

    return exclude_files([directory + "/" + file for file in os.listdir(directory)], type)

# Checks if source files have been changed.
def check_for_changes():

    sourcefiles = get_files(sourcedirectory, sourcetype)
    objectfiles = get_files(objectdirectory, objecttype)

    commandline = compilationcommand.split(" ") + sourcefiles

    if len(sourcefiles) != len(objectfiles):
        execute_command(commandline)

        # Moving object files.
        objectfiles = get_files(".", objecttype)
        execute_command(["mv"] + objectfiles + [objectdirectory])
        return

    compilelist = []

    # Reading sources and object files.
    for source, object in zip(sourcefiles, objectfiles):

        source_data = os.stat(source)
        object_data = os.stat(object)

        # Source files needs to be recompiled
        if source_data.st_mtime > object_data.st_mtime:
            compilelist.append(source)

    # source files needs to be recompiled.
    if len(compilelist):
        commandline = compilationcommand.split(" ") + compilelist
        execute_command(commandline)

        # Moving object files.
        objectfiles = get_files(".", objecttype)
        execute_command(["mv"] + objectfiles + [objectdirectory])


##############
### Config ###
##############

def check_dir(path):

    if os.path.isdir(path) == False:
        print(f"Coulndn't find the {path} directory.", file=sys.stderr)
        exit(1)

# Checks if the config file exists
def does_config_file_exists(func):

    if os.path.isfile(configfilepath):
        return func
    return create_config

# Create a config file where source and object files are stored.
def create_config():

    global sourcedirectory, objectdirectory, compilationcommand

    sourcedirectory    = input("Source directory: ")
    objectdirectory    = input("Object directory: ")
    compilationcommand = input("Compilation command: ")

    check_dir(sourcedirectory)
    check_dir(objectdirectory)

    with open(configfilepath, "w+") as file:
        file.write(sourcedirectory + "\n")
        file.write(objectdirectory + "\n")
        file.write(compilationcommand + "\n")

# Reading config file.
@does_config_file_exists
def read_config():

    global sourcedirectory, objectdirectory, compilationcommand

    with open(configfilepath, "r") as file:
        sourcedirectory = file.readline().replace('\n', '')
        objectdirectory = file.readline().replace('\n', '')
        compilationcommand = file.readline().replace('\n', '')

def display_help():
    print("usage: hot-reloading [-b | --build] [-h | --help]\n"\
          "\nRegenerates object files if source files has been changed.\n"\
          "     -b | --build :  build a binary\n"\
          "     -h | --help  :  display this help")

def main():

    if len(sys.argv) > 2:
        print("Invalid parameters.\n", file=sys.stderr)
        display_help()
        exit(1)

    elif len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        display_help()
        exit(0)

    elif len(sys.argv) == 2 and (sys.argv[1] == "-b" or sys.argv[1] == "--build"):

        ## To be implemented
        display_help()
        exit(0)

    read_config()
    check_for_changes()

if __name__ == "__main__":
    main()