"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the moment it breaks production:
a brutally honest postmortem confession, under 200 characters.
"""

import os
import tempfile

LINE = "I dropped the production database to free up disk space. The backups were on the same disk. My bad."


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in LINE or LINE != LINE.strip() or not LINE.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        os.replace(tmp, path)
    except OSError:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    print(LINE)


if __name__ == "__main__":
    main()
