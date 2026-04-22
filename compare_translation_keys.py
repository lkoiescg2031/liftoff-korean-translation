#!/usr/bin/env python3
"""Compare translation key coverage between the base and Korean CSV files."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def load_keys(csv_path: Path) -> list[str]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or "Keys" not in reader.fieldnames:
            raise ValueError(f"'Keys' column not found in {csv_path}")

        return [row["Keys"] for row in reader if row.get("Keys")]


def print_section(title: str, keys: list[str]) -> None:
    print(f"\n[{title}] ({len(keys)})")
    if not keys:
        print("-")
        return

    for key in keys:
        print(key)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare translation keys between the source CSV and ko CSV."
    )
    parser.add_argument(
        "base_csv",
        nargs="?",
        default="TranslationSpreadsheet.csv",
        help="Base/source CSV path (default: TranslationSpreadsheet.csv)",
    )
    parser.add_argument(
        "ko_csv",
        nargs="?",
        default="TranslationSpreadsheet.ko.csv",
        help="Korean CSV path (default: TranslationSpreadsheet.ko.csv)",
    )
    args = parser.parse_args()

    base_path = Path(args.base_csv)
    ko_path = Path(args.ko_csv)

    base_keys = set(load_keys(base_path))
    ko_keys = set(load_keys(ko_path))

    common_keys = sorted(base_keys & ko_keys)
    ko_only_keys = sorted(ko_keys - base_keys)
    missing_in_ko_keys = sorted(base_keys - ko_keys)

    print("Translation key comparison")
    print(f"- Base CSV: {base_path}")
    print(f"- KO CSV:   {ko_path}")
    print(f"- Base key count: {len(base_keys)}")
    print(f"- KO key count:   {len(ko_keys)}")

    print_section("Both files", common_keys)
    print_section("Only in ko file", ko_only_keys)
    print_section("Missing in ko file", missing_in_ko_keys)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
