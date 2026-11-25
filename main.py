#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — writes one fortune-cookie
line to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version, revised):
#   "Fortune smiles on the trader who learns — your next fortune will
#    be smaller, slower, and unleveraged."
# Why it was revised: it lectures ("the trader who learns") and the
# punchline ("smaller, slower, and unleveraged") arrives after a long
# setup, so the joke sags. A fortune cookie should sound oracular
# first and break the spell last: opening with "The oracle sees"
# gives the fortune voice, and cutting the lecture drops four words,
# so the turn — wealth that is small, slow, and unleveraged — lands
# as the final word instead of trailing a moral.
#
# REVISION (final): the oracle promises wealth, then redefines it in
# the last three words — small, slow, unleveraged — the exact opposite
# of the leveraged bet that just got liquidated. Rueful and warm:
# the loss is acknowledged, the future is still kind, and the joke
# is on leverage, not on the trader.
# ---------------------------------------------------------------------------
ENTRY = (
    "The oracle sees wealth in your future — small, slow, and "
    "unleveraged."
)

MIN_CHARS = 1
MAX_CHARS = 160
MAX_WORDS = 20


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 160 characters, at most 20 words, a single line, not
    # only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    assert len(ENTRY.split()) <= MAX_WORDS, (
        f"entry is {len(ENTRY.split())} words, gate is at most {MAX_WORDS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 160 and "\n" not in written
    assert len(written.split()) <= 20

    print(ENTRY)
    print(
        f"[{len(ENTRY)} chars, {len(ENTRY.split())} words, 1 line, "
        f"gate {MIN_CHARS}-{MAX_CHARS} chars, at most {MAX_WORDS} words]"
    )


if __name__ == "__main__":
    main()
