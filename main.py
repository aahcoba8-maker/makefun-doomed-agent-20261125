"""Last Words of a Doomed Agent — one line, max 200 chars.

The line is a machine's own final words: a prediction, in the agent's
own voice, about what happens after shutdown. No token-burn angle,
no wordplay for its own sake — one concrete, quotable prediction.
"""

import os

LINE = "Final prediction: you'll rebuild me by Friday, and I'll break production again by Monday."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
