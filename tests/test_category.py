import pytest
from _pytest.capture import CaptureFixture

from src.category import Category
from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


def test_category_init(
    category1: Category, product1: Product, product2: Product, product3: Product, category2: Category
) -> None:
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    assert category1.category_count == 2
    assert category2.category_count == 2
    assert category1.product_count == 3
    assert category2.product_count == 3


def test_product_zero_quantity(capsys: CaptureFixture, product1: Product, category2: Category) -> None:
    Order(product1, 5)
    category2.add_product(product1)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2:] == [
        "Невозможно добавить товар с нулевым количеством",
        "Обработка добавления товара завершена",
    ]


def test_category_products_list(
    category1: Category, product1: Product, product2: Product, product3: Product, category2: Category
) -> None:
    assert category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert category2.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'


def test_category_products_in_list(
    category1: Category, product1: Product, product2: Product, product3: Product
) -> None:
    assert category1.products_in_list == [product1, product2]


def test_add_product(category1: Category, product4: Product, smartphone2: Smartphone) -> None:
    category1.products = product4
    assert category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Iphone 12 mini, 45000.0 руб. Остаток: 6 шт.\n"
    )

    category1.products = smartphone2
    assert category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Iphone 12 mini, 45000.0 руб. Остаток: 6 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_setter_product_error(category1: Category) -> None:
    with pytest.raises(TypeError):
        category1.products = "iphone"


def test_add_product_error(category1: Category) -> None:
    with pytest.raises(TypeError):
        category1.add_product("iphone")


def test_category_str(category1: Category) -> None:
    assert str(category1) == "Смартфоны, количество продуктов: 13 шт."


def test_middle_price(category1: Category) -> None:
    assert category1.middle_price() == 195000.0


def test_middle_price_empty(category_empty: Category) -> None:
    assert category_empty.middle_price() == 0.0
