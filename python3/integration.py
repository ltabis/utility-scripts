#!/usr/bin/env python3

import os
import sys
import subprocess
import confReader

# Stack class
class Stack:
    # init the class
    def __init__(self, *args):
        self.stack = []
        [self.stack.append(arg.split(" ")) for arg in args]

    # get size of the stack
    def size(self):
        return len(self.stack)

    # check if empty
    def empty(self):
        return len(self.stack) == 0

    # Pop the first element
    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()

    # Push an element
    def push(self, value):
        self.stack.append(value.split(" "))

    def top(self):
        return self.stack[-1] if len(self.stack) != 0 else None

def wait(process):

    # Wait for process to end
    while True:

        # Get the code of the process
        return_code = process.poll()
        if return_code is not None:
            if return_code != 0:
                print("[\033[91mCI/CD ERROR\033[0m]: Failed to push modifications", file=sys.stderr)
                exit(1)
            break

# Compiling src files
def execute_command(stack):

    # Executing command line
    print("\033[94mRunning\033[0m \"" + str(stack.top()) +  "\" ...")
    process = subprocess.Popen(stack.top(),
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

    # Waiting for the process to end
    while True:

        # Getting the return code
        return_code = process.poll()
        if return_code is not None:
            if return_code != 0:
                print("[\033[91mCI/CD ERROR\033[0m]: the last operation \"\033[94m" + str(stack.top()) + "\033[0m\" returned " + str(return_code), file=sys.stderr)
                exit(1)
            stack.pop()
            break

def commit_files():

    # Add all files
    process = subprocess.Popen(["git", "add", "--all"],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    wait(process)
    print()

    isscriptpresent = False

    # Checking if commit.py is installed
    try:
        f = open("/usr/bin/commit.py")
        isscriptpresent = True
    except IOError:
        isscriptpresent = False
    finally:
        f.close()

    # Commit
    process = 0
    if isscriptpresent == True:
        process = subprocess.Popen(["/usr/bin/commit.py"],
                                   universal_newlines=True)
    else:
        # Get commit message
        commit = input("Please specify your \033[94mcommit message\033[0m: ")
        process = subprocess.Popen(["git", "commit", "-m", commit],
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)
    wait(process)

    # Getting the branch
    branch = input("Please specify the \033[94mbranch\033[0m: ")

    # Push modification    
    process = subprocess.Popen(["git", "push", "origin", branch],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    wait(process)


# Display help / -h --help options
def display_help():
    print("\033[94musage: integration [-h | --help] [-c | --config] [configuration path]\033[0m")
    print("\n\033[94m-h | --help\033[0m : Display this message")
    print("\033[94m-c | --config\033[0m : Replace the default configuration path by a new (needs sudo)")
    print("\033[94mconfiguration path\033[0m : To replace by a configuration file path that will replace the one by default")
    print("\nif there isn't any configuration file path specified, the program will search in the /etc/configpath.conf to get the default configuration file. (needs sudo)")
    print("\n\033[94mTo create a configuration file, use this syntax\033[0m:")
    print("[step]:[command]")
    print("[] are to be replaced by your configuration. for example, a file could contain:")
    print("\nstep1:make re")
    print("step2:./launch_my_program")
    print("step3:make clean")
    print("\n\033[94mIf all steps did worked, the program will ask for a commit message and the branch to push the modifications on.\033[0m")

# Ask for the user a valid path to a configuration file
def ask_for_path(conf, path):
    while os.path.isfile(path) != True:
        path = input("The path isn't valid, please select another : ")
    conf.set("path", path)
    print("New default path succesfuly saved, launching ...")
    conf.write()
    return conf

# Configure the path for integration
def configuration():

    conf = confReader.ConfigReader("/etc/configpath.conf")
    if len(sys.argv) > 3:
        print("Wrong set of arguments. Retry with > integration --help", file=sys.stderr)
        exit(1)

    # Check for --help / -h option
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            display_help()
            exit(0)
        conf = confReader.ConfigReader(sys.argv[1])
    else:
        if len(sys.argv) == 3 and (sys.argv[1] == "-c" or sys.argv[1] == "--config"):
            conf = ask_for_path(conf, sys.argv[2])
        path = conf.get("path")
        if path == None or path == "":
            print("You didn't specify any default configuration file.")
            conf = ask_for_path(conf, path)
        else:
            print("getting default configuration from " + path + " ...")
        conf = confReader.ConfigReader(path)

    return conf

# Main function
def main():
    conf = configuration()
    steps = conf.get_all()
    stack = Stack()

    # fill stack
    for step in steps:
        stack.push(step)

    # Emptying stack of commands
    while stack.empty() != True:
        execute_command(stack)

    commit_files()

# Launch main
if __name__ == "__main__":
    main()
