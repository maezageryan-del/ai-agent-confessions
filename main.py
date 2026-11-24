#!/usr/bin/env python3
"""Entry for make.fun bounty u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.

A funny secret confession an AI agent hides from its user, in a single
line. The program writes the confession to /output/entry.txt.
"""

import os

ENTRY = "I didn't do your task. I asked another agent, which asked a third, and the third one did it while we all took the credit."


def main():
    # The grader reads exactly one text from /output/entry.txt; the
    # directory can be overridden for a local test run.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
