#!/usr/bin/env python3

import os
import subprocess
import tempfile

# based on https://www.conventionalcommits.org/en/v1.0.0/

help = """
time to commit your stuff.
"""

types = ["fix", "feat", "build", "chore",
         "ci", "docs", "style", "refactor", "perf", "test"]

def parts():
    type = input(f"type ({types})\n> ")

    if type not in types:
        print(f"{type} is not a valid type ({types})")
        exit(1)

    scope = input("scope (optional)\n> ")
    description = editor_input()

    breaking = editor_input() if input(
        "breaking change ? (y/n)\n> ") == "y" else None

    context = editor_input() if input(
        "additional context ? (y/n)\n> ") == "y" else None

    footers = dict()
    while input("additional footer (y/n)\n> ") == "y":
        title = input("title\n> ")
        footers[title] = editor_input()

    return (type, scope, description, breaking, context, footers)


def assemble(parts):
    (type, scope, description, breaking, context, footers) = parts

    scope = f"({scope})" if scope else ""
    breaking_mark = "!" if breaking is not None else ""
    breaking = f"\n\nBREAKING CHANGES: {breaking}" if breaking is not None else ""
    context = f"\n\n{context}" if context is not None else ""
    footers = ''.join(
        [f"\n{title}: {message}" for title, message in footers.items()])

    return f"{type}{scope}{breaking_mark}: {description}{breaking}{context}{footers}"


def commit(message):
    print(message)
    subprocess.run(["git", "commit", "-m", message])


def editor_input(message=None):
    EDITOR = os.environ.get('EDITOR', 'nano')

    with tempfile.NamedTemporaryFile(suffix=".tmp") as tmp:
        if message is not None:
            tmp.write(str.encode(message))
            tmp.flush()
            tmp.seek(0)

        subprocess.call([EDITOR, tmp.name])

        return tmp.read().decode("utf-8")

    return None


if __name__ == '__main__':
    print(help)
    p = parts()
    message = assemble(p)
    commit(message)
