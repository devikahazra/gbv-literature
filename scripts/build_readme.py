#!/usr/bin/env python3
"""Regenerate the papers table in README.md from data/papers.csv.

The table is written between the <!-- TABLE:START --> and <!-- TABLE:END -->
markers in README.md. Run from the repo root:

    python scripts/build_readme.py
"""
import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "papers.csv"
README = ROOT / "README.md"
START, END = "<!-- TABLE:START -->", "<!-- TABLE:END -->"


def esc(cell: str) -> str:
    return cell.replace("|", "\\|").replace("\n", " ").strip()


def build_table() -> str:
    with CSV.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows:
        return "_No papers yet._"
    header, *body = rows
    lines = ["| " + " | ".join(header) + " |",
             "|" + "|".join(["---"] * len(header)) + "|"]
    for r in body:
        r += [""] * (len(header) - len(r))
        lines.append("| " + " | ".join(esc(c) for c in r) + " |")
    count = len(body)
    note = f"\n\n**{count} paper{'s' if count != 1 else ''} listed.**"
    return "\n".join(lines) + note


def main() -> None:
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit("Markers not found in README.md")
    pre = text.split(START)[0]
    post = text.split(END)[1]
    README.write_text(f"{pre}{START}\n\n{build_table()}\n\n{END}{post}",
                       encoding="utf-8")
    print("README.md table updated.")


if __name__ == "__main__":
    main()
