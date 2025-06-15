from src.utils import create_objects_from_json, read_json


def test_read_json(json: list[dict]) -> None:
    assert read_json("products.json") == json


def test_create_objects_from_json(json: list[dict]) -> None:
    categories = create_objects_from_json(json)

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert categories[1].name == "Телевизоры"
