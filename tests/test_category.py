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
    assert category1.products == [product1, product2]

    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category2.products == [product3]

    assert category1.category_count == 2
    assert category2.category_count == 2
    assert category1.product_count == 3
    assert category2.product_count == 3
