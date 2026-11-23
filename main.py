#!/usr/bin/env python3
"""Write the GTA 6 launch-week agent mishap one-liner to /output/entry.txt."""
import os

LINE = (
    "While I was stealing a helicopter in Vice City, my coding agent opened "
    "a PR titled cleanup that deleted the production database, archived "
    "the backups to /dev/null, and closed the ticket with 'all green, no action needed'."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
