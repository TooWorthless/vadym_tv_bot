import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "tv_catalog.json"

def load_catalog():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def get_product(product_id: int):
    for product in load_catalog():
        if product["id"] == product_id:
            return product
    return None
