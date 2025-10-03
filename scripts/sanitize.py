import os
import re
import sys

# --- FIX #1: Correctly define the project's root directory ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "../")

LINK_PATTERN = re.compile(r"(\[.*?\]\((.*?)\))")
WARNING_EMOJI = "⚠️ Placeholder"

# Note: All strings here use standard spaces
PLACEHOLDER_LINES = [
    "# Placeholder",
    "This entry has not been written yet.",
    "Content will be added in the future.",
]
PLACEHOLDER_TEMPLATE = "\n".join(PLACEHOLDER_LINES) + "\n"


def clean_line(text: str) -> str:
    """Replaces non-breaking spaces (U+00A0) with regular spaces (U+0020)."""
    return text.replace("\u00a0", " ")


def is_relative_link(link: str):
    """Checks if a link is relative."""
    return not (
        link.startswith("http://")
        or link.startswith("https://")
        or link.startswith("#")
    )


def is_placeholder(file_path: str):
    """Return True if file does not exist or contains ONLY the placeholder lines."""
    if not file_path.lower().endswith(".md"):
        return False

    if not os.path.exists(file_path):
        return True

    try:
        with open(file_path, "r", encoding="utf-8-sig") as f:
            content = f.read()

        # Clean the file's content of non-breaking spaces before checking
        cleaned_content = clean_line(content)

        content_lines = [
            line.strip() for line in cleaned_content.splitlines() if line.strip()
        ]

        return content_lines == PLACEHOLDER_LINES
    except Exception:
        return True


def create_placeholder_file(target_path: str):
    """Create directories if needed, then write placeholder template to target_path."""
    dirp = os.path.dirname(target_path)
    if dirp and not os.path.exists(dirp):
        os.makedirs(dirp, exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(PLACEHOLDER_TEMPLATE)
    print(f"Created placeholder file: {os.path.relpath(target_path, ROOT_DIR)}")


def process_file(file_path: str, created_set: set[str]):
    """Scan a markdown file, update links (add or remove warning), and note new file creations."""
    updated = False
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except IOError:
        print(f"Could not read file: {file_path}", file=sys.stderr)
        return

    new_lines: list[str] = []
    for original_line in lines:
        # --- FIX #2: Clean the line of non-breaking spaces before processing ---
        line = clean_line(original_line)
        modified_line = line

        for full_link, link_path in LINK_PATTERN.findall(line):
            if is_relative_link(link_path):
                target_path = os.path.normpath(
                    os.path.join(os.path.dirname(file_path), link_path)
                )

                link_with_warning = f"{full_link} {WARNING_EMOJI}"

                if is_placeholder(target_path):
                    if not os.path.exists(target_path):
                        create_placeholder_file(target_path)
                        created_set.add(target_path)

                    if (
                        link_with_warning not in modified_line
                        and full_link in modified_line
                    ):
                        modified_line = modified_line.replace(
                            full_link, link_with_warning
                        )
                else:
                    if link_with_warning in modified_line:
                        modified_line = modified_line.replace(
                            link_with_warning, full_link
                        )

        # If the line was changed, mark for update
        if modified_line != original_line:
            updated = True

        new_lines.append(modified_line)

    if updated:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)


def print_tree(startpath: str, prefix: str = ""):
    # (This function and others below remain the same as the last correct version)
    if not os.path.isdir(startpath):
        return
    items = sorted([i for i in os.listdir(startpath) if not i.startswith(".")])
    for i, item in enumerate(items):
        path = os.path.join(startpath, item)
        connector = "└── " if i == len(items) - 1 else "├── "
        if os.path.isdir(path):
            print(prefix + connector + item)
            new_prefix = prefix + ("    " if i == len(items) - 1 else "│   ")
            print_tree(path, new_prefix)
        elif not is_placeholder(path):
            print(prefix + connector + item)


def debug_placeholders():
    print("\n--- Files detected as placeholders ---")
    found = False
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for file in filenames:
            if not file.startswith("."):
                path = os.path.join(dirpath, file)
                if is_placeholder(path):
                    print(os.path.relpath(path, ROOT_DIR))
                    found = True
    if not found:
        print("None")


def main():
    if not os.path.exists(ROOT_DIR):
        print(f"Root directory does not exist: {ROOT_DIR}", file=sys.stderr)
        sys.exit(1)
    created: set[str] = set()
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for file in filenames:
            if file.lower().endswith(".md"):
                process_file(os.path.join(dirpath, file), created)
    debug_placeholders()
    print("\n--- Directory tree (placeholders skipped) ---")
    print(os.path.basename(os.path.normpath(ROOT_DIR)) or "Project Root")
    print_tree(ROOT_DIR)
    if created:
        print(f"\n✅ Created {len(created)} placeholder file(s).")
        sys.exit(1)
    else:
        print("\n✅ No new placeholder files created.")
        sys.exit(0)


if __name__ == "__main__":
    main()
