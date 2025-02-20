import json
from Restaurante.Menu import *
from typing import Dict


#* Clase para manejar los menus
class MenuManager:
    def __init__(self, menu_file: str = "menu.json"):
        self.menu_file = menu_file
        self.menu = self.load_menu()

    #* Cargar el menú desde un archivo JSON
    def load_menu(self) -> Dict:
        try:
            with open(self.menu_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    #* Guardar el menú en un archivo JSON
    def save_menu(self):
        with open(self.menu_file, "w") as file:
            json.dump(self.menu, file, indent=4)

    #* Crear un nuevo menú
    def create_menu(self, menu_name: str):
        if menu_name not in self.menu:
            self.menu[menu_name] = []
            self.save_menu()
            print(f"Menú '{menu_name}' creado exitosamente.")
        else:
            print(f"El menú '{menu_name}' ya existe.")

    #* Agregar un ítem al menú
    def add_item_to_menu(self, menu_name: str, item: MenuItem):
        if menu_name in self.menu:
            item_dict = {
                "name": item.name,
                "price": item.price,
                "type": item.__class__.__name__,  
                "size": getattr(item, "size", None),
                "protein_choice": getattr(item, "protein_choice", None),
                "extra_portion": getattr(item, "extra_portion", None),  
                "topping": getattr(item, "topping", None)
            }
            self.menu[menu_name].append(item_dict)
            self.save_menu()
            print(f"Ítem '{item.name}' agregado al menú '{menu_name}'.")
        else:
            print(f"El menú '{menu_name}' no existe.")

    #* Actualizar un ítem en el menú
    def update_item_in_menu(self, menu_name: str, item_index: int, new_item: MenuItem):
        if menu_name in self.menu:
            if 0 <= item_index < len(self.menu[menu_name]):
                new_item_dict = {
                    "name": new_item.name,
                    "price": new_item.price,
                    "type": new_item.__class__.__name__,
                    "size": getattr(new_item, "size", None),
                    "protein_choice": getattr(new_item, "protein_choice", None),
                    "extra_portion": getattr(new_item, "extra_portion", None),
                    "topping": getattr(new_item, "topping", None)
                }
                self.menu[menu_name][item_index] = new_item_dict
                self.save_menu()
                print(f"Ítem actualizado en el menú '{menu_name}'.")
            else:
                print(f"Índice {item_index} fuera de rango en el menú '{menu_name}'.")
        else:
            print(f"El menú '{menu_name}' no existe.")

    #* Eliminar un ítem del menú
    def delete_item_from_menu(self, menu_name: str, item_index: int):
        if menu_name in self.menu:
            if 0 <= item_index < len(self.menu[menu_name]):
                deleted_item = self.menu[menu_name].pop(item_index)
                self.save_menu()
                print(f"Ítem '{deleted_item['name']}' eliminado del menú '{menu_name}'.")
            else:
                print(f"Índice {item_index} fuera de rango en el menú '{menu_name}'.")
        else:
            print(f"El menú '{menu_name}' no existe.")

    #* Mostrar un menú
    def show_menu(self, menu_name: str):
        if menu_name in self.menu:
            print(f"Menú '{menu_name}':")
            for index, item in enumerate(self.menu[menu_name]):
                print(f"{index}: {item}")
        else:
            print(f"El menú '{menu_name}' no existe.")
        


#* Convertir un diccionario en un ítem del menú
def dict_to_item(item_dict: Dict) -> MenuItem:
    item_type = item_dict.get("type")
    name = item_dict.get("name")
    price = item_dict.get("price")

    if item_type == "Beverage":
        size = item_dict.get("size")
        return Beverage(name=name, price=price, size=size)
    elif item_type == "MainDish":
        protein_choice = item_dict.get("protein_choice")
        return MainDish(name=name, price=price, protein_choice=protein_choice)
    elif item_type == "Starters":
        extra_portion = item_dict.get("extra_portion")
        return Starters(name=name, price=price, extra_portion=extra_portion)
    elif item_type == "Desserts":
        topping = item_dict.get("topping")
        return Desserts(name=name, price=price, topping=topping)
    else:
        raise ValueError(f"Tipo de ítem no válido: {item_type}")