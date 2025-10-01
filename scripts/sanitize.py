import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "../")

LINK_PATTERN = re.compile(r"(\[.*?\]\((.*?)\))")
WARNING_EMOJI = "⚠️ Placeholder"

PLACEHOLDER_LINES = [
    "# Placeholder",
    "This entry has not been written yet.",
    "Content will be added in the future.",
]

PLACEHOLDER_TEMPLATE = "\n".join(PLACEHOLDER_LINES) + "\n"


def is_relative_link(link):
    return not (
        link.startswith("http://")
        or link.startswith("https://")
        or link.startswith("#")
    )


def is_placeholder(file_path):
    """Return True if file does not exist or contains the placeholder lines in order."""
    if not file_path.lower().endswith(".md"):
        return False

    if not os.path.exists(file_path):
        return True

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        content_lines = [
            line.strip()
            for line in content.replace("\r\n", "\n").split("\n")
            if line.strip()
        ]

        idx = 0
        for line in content_lines:
            if idx < len(PLACEHOLDER_LINES) and line == PLACEHOLDER_LINES[idx]:
                idx += 1
            if idx == len(PLACEHOLDER_LINES):
                return True
        return False
    except Exception as e:
        return True


def create_placeholder_file(target_path):
    """Create directories if needed, then write placeholder template to target_path."""
    dirp = os.path.dirname(target_path)
    if dirp and not os.path.exists(dirp):
        os.makedirs(dirp, exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(PLACEHOLDER_TEMPLATE)
    print(f"Created placeholder file: {target_path}")


def process_file(file_path, created_set):
    """Scan a markdown file, update links (add or remove warning), and note new file creations."""
    updated = False
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        matches = LINK_PATTERN.findall(line)
        for full_link, link_path in matches:
            if is_relative_link(link_path):
                target_path = os.path.normpath(
                    os.path.join(os.path.dirname(file_path), link_path)
                )
                if is_placeholder(target_path):
                    if not os.path.exists(target_path):
                        create_placeholder_file(target_path)
                        created_set.add(target_path)
                    if WARNING_EMOJI not in line:
                        line = line.replace(full_link, f"{full_link} {WARNING_EMOJI}")
                        updated = True
                else:
                    if WARNING_EMOJI in line:
                        line = line.replace(f" {WARNING_EMOJI}", "")
                        updated = True
        new_lines.append(line)

    if updated:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)


def print_tree(startpath, prefix=""):
    """Print a directory tree while skipping placeholder files and hidden items."""
    items = sorted([i for i in os.listdir(startpath) if not i.startswith(".")])
    for i, item in enumerate(items):
        path = os.path.join(startpath, item)
        connector = "└── " if i == len(items) - 1 else "├── "
        if os.path.isdir(path):
            print(prefix + connector + item)
            new_prefix = prefix + ("    " if i == len(items) - 1 else "│   ")
            print_tree(path, new_prefix)
        else:
            if not is_placeholder(path):
                print(prefix + connector + item)


def debug_placeholders():
    """Print all files that are being detected as placeholders."""
    print("\nFiles detected as placeholders:\n")
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]

        for file in filenames:
            if file.startswith("."):
                continue
            path = os.path.join(dirpath, file)
            if is_placeholder(path):
                print(os.path.relpath(path, ROOT_DIR))


def main():
    if not os.path.exists(ROOT_DIR):
        print(f"Root directory does not exist: {ROOT_DIR}")
        sys.exit(0)

    created = set()

    for dirpath, _, filenames in os.walk(ROOT_DIR):
        if any(part.startswith(".") for part in dirpath.split(os.sep)):
            continue
        for file in filenames:
            if file.lower().endswith(".md"):
                process_file(os.path.join(dirpath, file), created)

    debug_placeholders()

    print("\nDirectory tree (placeholders skipped):\n")
    print(os.path.basename(ROOT_DIR))
    print_tree(ROOT_DIR)

    if created:
        print(f"\nCreated {len(created)} placeholder file(s).")
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
