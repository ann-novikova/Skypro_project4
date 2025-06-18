import json
import os

from src.category import Category
from src.product import Product

path_to_files = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def read_json(filename: str) -> list[dict]:
    """Функция для чтения json файла и возврата списка словарей"""

    full_path = os.path.join(path_to_files, filename)
    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    else:
        return [{}]


def create_objects_from_json(info_objects: list[dict]) -> list:
    """Функция для создания классов их списка словарей"""

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
