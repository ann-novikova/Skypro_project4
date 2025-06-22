from typing import Any

from src.base_category import BaseCategory
from src.product import Product
from src.zero_expeption import ZeroQuantityException


class Category(BaseCategory):
    """Класс категория для группировки продуктов"""

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        try:
            for product in products:
                if product.quantity == 0:
                    raise ZeroQuantityException('Невозможно добавить товар с нулевым количеством')
        except ZeroQuantityException as e:
            print(str(e))
        else:
            self.__products = products
            print('Товар добавлен')
        finally:
            print('Обработка добавления товара завершена')

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        product_quantity = 0
        for product in self.__products:
            product_quantity += product.quantity
        return f"{self.name}, количество продуктов: {product_quantity} шт."

    def add_product(self, product: Any) -> None:
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityException('Невозможно добавить товар с нулевым количеством')
            except ZeroQuantityException as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print('Товар добавлен')
            finally:
                print('Обработка добавления товара завершена')
        else:
            raise TypeError

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @products.setter
    def products(self, product: Any) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")
        self.add_product(product)

    @property
    def products_in_list(self) -> list:
        return self.__products

    def middle_price(self):
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products),2)
        except ZeroDivisionError:
            return float(0)
