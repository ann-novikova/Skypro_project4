from typing import Any

from src.category import Category


class ProductIterator:
    """Вспомогательный класс для перебора товаров из категорий"""

    def __init__(self, product_category: Category):
        self.category = product_category
        self.index = 0

    def __iter__(self) -> "ProductIterator":
        self.index = 0
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
