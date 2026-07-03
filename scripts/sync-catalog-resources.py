#!/usr/bin/env python3
"""Mirror catalog data into Hugo asset resources for server-side templates."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
ASSET_DIR = ROOT / "assets" / "catalog"


def main() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)

    with (DATA_DIR / "products.csv").open(newline="", encoding="utf-8") as products_file:
        products = list(csv.DictReader(products_file))

    (ASSET_DIR / "products.json").write_text(
        json.dumps(products, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    (ASSET_DIR / "product-images.json").write_text(
        (DATA_DIR / "product-images.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
