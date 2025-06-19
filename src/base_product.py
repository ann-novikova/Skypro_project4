from abc import ABC, abstractmethod

class BaseProduct(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> None:
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> None:
        pass

    @property
    @abstractmethod
    def price(self) -> None:
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        pass
