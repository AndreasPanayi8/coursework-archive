#!/usr/bin/env python3
import os, json

ROOT = os.getcwd()

IGNORE_DIRS = {".git", ".github", ".meta", "__pycache__"}
IGNORE_FILES = set()s


def walk(path):
    items = sorted(os.listdir(path))
    files = []
    dirs = []

    for x in items:
        xp = os.path.join(path, x)
        if os.path.isdir(xp):
            if x in IGNORE_DIRS:
                continue
            dirs.append(x)
        else:
            if x in IGNORE_FILES:
                continue
            files.append(x)

    children = []
    for d in dirs:
        children.append(walk(os.path.join(path, d)))

    return {
        "name": os.path.basename(path),
        "path": os.path.relpath(path, ROOT),
        "files": files,
        "dirs": children
    }

if __name__ == "__main__":
    data = walk(ROOT)
    with open("manifest.json", "w") as f:
        json.dump(data, f, indent=2)
    print("manifest.json updated.")
