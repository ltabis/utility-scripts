#!/usr/bin/env python3

import configparser
from ntpath import join
import sys
import os

# based on https://www.conventionalcommits.org/en/v1.0.0/

help = """
time to commit your stuff.
"""

types = ["fix", "feat", "BREAKING CHANGE", "build", "chore",
         "ci", "docs", "style", "refactor", "perf", "test"]

# Ask for a multiline message.


def multiline(section):
    print(f"{section} (type your message, newline + '.' to stop)")
    message = ""
    while True:
        part = input()
        if part == ".":
            return message
        else:
            message += f"{part}\n"

# get parts of the commit message.


def parts():
    type = input(f"type ({types})\n> ")

    if type not in types:
        print(f"{type} is not a valid type ({types})")
        exit(1)

    scope = input("scope (optional)\n> ")
    description = input("description\n> ")

    breaking = multiline("breaking changes") if input(
        "breaking change ? (y/n)\n> ") == "y" else None

    context = multiline("additional context") if input(
        "additional context ? (y/n)\n> ") == "y" else None

    footers = dict()
    while input("additional footer (y/n)\n> ") == "y":
        title = input("title\n> ")
        footers[title] = multiline("footer content")

    return (type, scope, description, breaking, context, footers)

# assemble the commit message.


def assemble(parts):
    (type, scope, description, breaking, context, footers) = parts

    scope = f"({scope})" if scope else ""
    breaking_mark = "!" if breaking is not None else ""
    breaking = f"\n\nBREAKING CHANGES: {breaking}" if breaking is not None else ""
    context = f"\n\n{context}" if context is not None else ""
    footers = ''.join(
        [f"\n{title}: {message}" for title, message in footers.items()])

    return f"{type}{scope}{breaking_mark}: {description}{breaking}{context}{footers}"

# use git to commit the message.


def commit(message):
    print(message)
    os.system(repr(f'git commit -m "$(echo -e "{message}")"'))


if __name__ == '__main__':
    print(help)
    p = parts()
    message = assemble(p)
    commit(message)
