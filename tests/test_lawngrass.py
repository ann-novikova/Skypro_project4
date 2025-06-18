import pytest

from src.lawngrass import LawnGrass


def test_lawngrass_init(lawngrass1: LawnGrass) -> None:
    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.description == "Элитная трава для газона"
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20

    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
    assert lawngrass1.color == "Зеленый"

def test_lawngrass_add(lawngrass1: LawnGrass, lawngrass2: LawnGrass) -> None:
    assert lawngrass1 + lawngrass2 == 16750.0

def test_smartphone_add_error(smartphone1, lawngrass1, product1):
    with pytest.raises(TypeError):
        lawngrass1 + smartphone1
        lawngrass1 + product1
        lawngrass1 + 1