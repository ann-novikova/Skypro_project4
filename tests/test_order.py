from _pytest.capture import CaptureFixture

from src.order import Order
from src.product import Product


def test_order_init(order1: Order) -> None:
    assert order1.product.name == "Samsung Galaxy S23 Ultra"
    assert order1.sold_quantity == 2


def test_order_get_total_cost(order1: Order) -> None:
    assert order1.get_total_cost() == 360000.0


def test_order_str(order1: Order) -> None:
    assert str(order1) == "ID: 1, количество проданных продуктов: 2 шт., итоговая стоимость 360000.0"

def test_product_zero_quantity(capsys: CaptureFixture, product1: Product) -> None:
    order_test = Order(product1, 5)
    order_test2 = Order(product1, 1)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2:] == ['Невозможно добавить товар с нулевым количеством',
                                               'Обработка добавления товара завершена']
