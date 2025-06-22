from unittest.mock import Mock, patch

import pytest
from _pytest.capture import CaptureFixture

from src.product import Product


def test_product_init(capsys: CaptureFixture, product1: Product, product2: Product) -> None:
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8

    message = capsys.readouterr()
    assert message.out.strip() == (
        "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)\n"
        "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"
    )


def test_new_product(new_product: dict) -> None:
    product5 = Product.new_product(new_product)
    assert product5.quantity == 18
    assert product5.price == 250000.0


def test_price_setter_zero(capsys: pytest.CaptureFixture[str], product1: Product) -> None:
    product1.price = 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


@patch("builtins.input")
def test_price_setter_low(mock_input: Mock, product1: Product) -> None:
    mock_input.return_value = "y"
    product1.price = 150000.0
    assert product1.price == 150000.0


@patch("builtins.input")
def test_price_setter_low_not_confirmed(mock_input: Mock, product1: Product) -> None:
    mock_input.return_value = "n"
    product1.price = 150000.0
    assert product1.price == 180000.0


def test_products_str(product1: Product) -> None:
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_products_add(product1: Product, product2: Product) -> None:
    assert product1 + product2 == 2580000.0
