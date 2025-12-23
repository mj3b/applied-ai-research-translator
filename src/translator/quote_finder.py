from pathlib import Path
import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--text", required=True)
    p.add_argument("--query", required=True)
    p.add_argument("--context", type=int, default=2)
    p.add_argument("--max", type=int, default=10)
    args = p.parse_args()

    lines = Path(args.text).read_text(encoding="utf-8", errors="ignore").splitlines()
    q = args.query.lower()

    hits = [i for i, line in enumerate(lines) if q in line.lower()]
    if not hits:
        print("No matches found.")
        return

    print(f"Found {len(hits)} matches. Showing up to {args.max}.\n")
    for k, i in enumerate(hits[: args.max], start=1):
        start = max(0, i - args.context)
        end = min(len(lines), i + args.context + 1)
        print(f"--- Match {k}: lines {start+1}-{end} ---")
        for j in range(start, end):
            prefix = ">> " if j == i else "   "
            print(f"{prefix}{j+1:>5}: {lines[j]}")
        print()

if __name__ == "__main__":
    main()
