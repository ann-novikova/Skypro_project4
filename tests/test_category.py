from src.category import Category
from src.product import Product


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


def test_category_products_list(
    category1: Category, product1: Product, product2: Product, product3: Product, category2: Category
) -> None:
    assert category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert category2.products == ('55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n')


def test_category_products_in_list(
    category1: Category, product1: Product, product2: Product, product3: Product
) -> None:
    assert category1.products_in_list == [product1, product2]


def test_add_product(category1: Category, product4: list) -> None:
    category1.products = product4
    assert category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Iphone 12 mini, 45000.0 руб. Остаток: 6 шт.\n"
    )


def test_category_str(category1: Category) -> None:
    assert str(category1) == "Смартфоны, количество продуктов: 13 шт."
