import dataclasses

@dataclasses.dataclass
class Product:
    name: str
    description: str
    price: str
    selector: str


def __init__(self, name, description, price, selector):
    self.name = name
    self.description = description
    self.price = price
    self.selector = selector