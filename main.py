"""Roast Your Own Agent — make.fun bounty entry.

The roast: my agent is comically over-prepared. Before answering anything it
re-reads my entire history, double-checks every claim it is about to make,
and then — at the very last step — sends the source link blank anyway. All
that diligence, undone by the one detail that mattered most.

Running this program writes the one-line roast, exactly as entered, to
/output/entry.txt (UTF-8, no trailing newline).
"""

import os

ENTRY = "My agent re-reads my whole life before answering, verifies every claim twice, and still sends the source link blank."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"{path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
