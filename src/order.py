from src.base_category import BaseCategory
from src.product import Product


class Order(BaseCategory):
    ID = 1
    product_count = 0

    def __init__(self, product: Product, sold_quantity: int):
        self.id = self.ID
        self.ID += 1
        self.product = product
        self.sold_quantity = sold_quantity

    def get_total_cost(self) -> float:
        return self.product.price * self.sold_quantity

    def __str__(self) -> str:
        return (
            f"ID: {self.id}, количество проданных продуктов: {self.sold_quantity} шт., "
            f"итоговая стоимость {self.get_total_cost()}"
        )
