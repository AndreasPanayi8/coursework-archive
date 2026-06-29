#!/usr/bin/env python3
import os, json, fnmatch

ROOT = os.getcwd()

# ── What to leave OUT of the manifest ──────────────────────────────────────
# Directories skipped entirely, along with everything inside them.
IGNORE_DIRS = {
    ".git", ".github", ".meta", "__pycache__",   # (originals)
    ".idea", ".vscode",                           # editor folders
}

# Exact filenames to skip. Only real OS junk here now — everything else
# (LICENSE, README.md, index.html, manifest.json, gen_manifest.py,
#  og-image.png, the CV PDFs, all content) stays visible.
IGNORE_FILES = {
    ".DS_Store", "Thumbs.db", "desktop.ini",      # OS junk
}

# Glob patterns to skip. The ".*" rule hides every dotfile
# (.DS_Store, .gitignore, .nojekyll, etc.) without listing each one.
IGNORE_PATTERNS = [".*", "*.pyc", "*.tmp"]


def skip(name):
    if name in IGNORE_FILES or name in IGNORE_DIRS:
        return True
    return any(fnmatch.fnmatch(name, pat) for pat in IGNORE_PATTERNS)


def walk(path):
    items = sorted(os.listdir(path))
    files = []
    dirs = []

    for x in items:
        if skip(x):
            continue
        xp = os.path.join(path, x)
        if os.path.isdir(xp):
            dirs.append(x)
        else:
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
        # ensure_ascii=False keeps any Greek / accented filenames readable
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("manifest.json updated.")
