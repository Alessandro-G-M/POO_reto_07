from collections import namedtuple

MenuItemTuple = namedtuple("MenuItemTuple", ["name", "price", "size", "protein_choice", "extra_portion", "topping"])

#* Clase padre de los ítems del menú
class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price})"
    
    def to_tuple(self):
        """Convierte la instancia en un namedtuple."""
        return MenuItemTuple(
            name=self.name,
            price=self.price,
            size=None,
            protein_choice=None,
            extra_portion=False,
            topping=None
        )


#* Bebidas
class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str = 'Normal'):
        if size.upper() == 'GRANDE':
            price += 1000
        elif size.upper() == 'PEQUEÑO':
            price -= 1000
        super().__init__(name, price)
        self.size = size.upper()

    def __str__(self):
        return f"{self.name} ({self.size}) (${self.price})"


#* Plato Principal
class MainDish(MenuItem):
    def __init__(self, name: str, price: float, protein_choice: str = 'chicken'):
        if protein_choice.upper() == 'BEEF':
            price += 3000
        elif protein_choice.upper() == 'SEAFOOD':
            price += 2500
        super().__init__(name, price)
        self.protein_choice = protein_choice.upper()

    def __str__(self):
        return f"{self.name} ({self.protein_choice}) (${self.price})"


#* Entradas
class Starters(MenuItem):
    def __init__(self, name: str, price: float, extra_portion: bool = False):
        if extra_portion:
            price += 2000
        super().__init__(name, price)
        self.extra_portion = extra_portion

    def __str__(self):
        extra = "Extra" if self.extra_portion else "Normal"
        return f"{self.name} ({extra}) (${self.price})"


#* Postres
class Desserts(MenuItem):
    def __init__(self, name: str, price: float, topping: str = 'none'):
        if topping.upper() == 'CHOCOLATE':
            price += 500
        elif topping.upper() == 'CARAMEL':
            price += 1000
        elif topping.upper() == 'NUTS':
            price += 1200
        super().__init__(name, price)
        self.topping = topping.upper()

    def __str__(self):
        return f"{self.name} ({self.topping}) (${self.price})"
