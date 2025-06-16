class Product:
    name: str
    description: str
    price: float
    quantity: int

    product_list: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.product_list.append({"name": name, "description": description, "price": price, "quantity": quantity})

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, new_product: dict) -> "Product":
        for product in Product.product_list:
            if product.get("name") == new_product.get("name"):
                name = new_product.get("name", "")
                description = new_product.get("description", "")
                price_new = new_product.get("price", 0.0)
                price_old = product.get("price", 0.0)
                quantity_new = new_product.get("quantity", 0)
                quantity_old = product.get("quantity", 0)
                price = price_new if price_new >= price_old else price_old
                quantity = quantity_new + quantity_old

                return cls(name, description, price, quantity)

        return cls(**new_product)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            price_confirmation = input("Вы подтверждаете что новая цена ниже? y/n")
            if price_confirmation.lower() == "y":
                self.__price = new_price
            else:
                print("Действие отменено")
                return
