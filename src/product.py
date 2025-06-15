class Product:
    name: str
    description: str
    price: float
    quantity: int

    product_list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.product_list.append({"name": name, "description": description, "price": price, "quantity": quantity})

    @classmethod
    def new_product(cls, new_product: dict):
        for product in Product.product_list:
            if product.get("name") == new_product.get("name"):
                return cls(
                    new_product.get("name"),
                    new_product.get("description"),
                    (
                        new_product.get("price")
                        if new_product.get("price") >= product.get("price")
                        else product.get("price")
                    ),
                    new_product.get("quantity") + product.get("quantity"),
                )
        return cls(**new_product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
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
