import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[dict]:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    else:
        return [{}]


def create_objects_from_json(info_objects: list[dict]) -> list:
    categories = []
    for category in info_objects:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    data = read_json("../data/products.json")
    products_info = create_objects_from_json(data)
    print(data)
