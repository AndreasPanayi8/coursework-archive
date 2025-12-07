import json
from pathlib import Path

root = Path('.')
entries = []

# Map categories to actual folder names
folders = {
    "Presentations": "0. Presentations",
    "Personal Projects": "1. Notes Writting",
    "Solved Exercises": "2. Exercises and Labs by Course"
}

for category, folder in folders.items():
    path = root / folder
    if not path.exists():
        print(f"Warning: folder '{folder}' does not exist")
        continue
    for f in path.rglob('*.*'):  # recursively find all files
        title = f.stem
        course = f.parent.name  # will use the immediate folder name for course
        entries.append({
            "src": str(f).replace("\\", "/"),
            "title": title,
            "category": category,
            "course": course
        })

with open('manifest.json', 'w') as out:
    json.dump(entries, out, indent=2)

print(f"{len(entries)} entries written to manifest.json")

