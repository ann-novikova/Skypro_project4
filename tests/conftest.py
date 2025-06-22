import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.order import Order
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


@pytest.fixture()
def product1() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product2() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product3() -> Product:
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture()
def smartphone1() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture()
def smartphone2() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture()
def lawngrass1() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def lawngrass2() -> LawnGrass:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture()
def product4() -> Product:
    return Product("Iphone 12 mini", "Фоновая подсветка", 45000.0, 6)


@pytest.fixture()
def new_product() -> dict[str, str | float]:
    return {"name": "Iphone 15", "description": "512GB, Gray space", "price": 250000.0, "quantity": 10}


@pytest.fixture()
def category1(product1: Product, product2: Product) -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )


@pytest.fixture()
def category2(product3: Product) -> Category:
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product3],
    )


@pytest.fixture()
def category_empty() -> Category:
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [],
    )


@pytest.fixture()
def order1(product1: Product) -> Order:
    return Order(product1, 2)


@pytest.fixture()
def product_iterator(category1: Category) -> ProductIterator:
    return ProductIterator(category1)


@pytest.fixture()
def json() -> list[dict]:
    return [
        {
            "name": "Смартфоны",
            "description": (
                "Смартфоны, как средство не только коммуникации, "
                "но и получение дополнительных функций для удобства жизни"
            ),
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14,
                },
            ],
        },
        {
            "name": "Телевизоры",
            "description": (
                "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником"
            ),
            "products": [
                {
                    "name": '55" QLED 4K',
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7,
                }
            ],
        },
    ]
