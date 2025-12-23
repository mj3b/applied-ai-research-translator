from pathlib import Path
import argparse

def load_lines(path: str) -> list[str]:
    return Path(path).read_text(encoding="utf-8", errors="ignore").splitlines()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--text", required=True, help="Path to paper_text.txt")
    p.add_argument("--query", required=True, help="Keyword/phrase to search for (case-insensitive)")
    p.add_argument("--context", type=int, default=2, help="Lines of context before/after match")
    p.add_argument("--max", type=int, default=10, help="Max matches to print")
    args = p.parse_args()

    lines = load_lines(args.text)
    q = args.query.lower()
    matches = []
    for i, line in enumerate(lines):
        if q in line.lower():
            matches.append(i)

    if not matches:
        print("No matches found.")
        return

    print(f"Found {len(matches)} matches. Showing up to {args.max}.\n")
    for idx, i in enumerate(matches[: args.max], start=1):
        start = max(0, i - args.context)
        end = min(len(lines), i + args.context + 1)
        print(f"--- Match {idx}: lines {start+1}-{end} ---")
        for j in range(start, end):
            prefix = ">> " if j == i else "   "
            print(f"{prefix}{j+1:>5}: {lines[j]}")
        print()

if __name__ == "__main__":
    main()
