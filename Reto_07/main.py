from Restaurante.Menu_Manager import MenuManager, dict_to_item
from Restaurante.Menu import Beverage, MainDish, Starters, Desserts
from Restaurante.Order_Manager import OrderManager, Order

def main():
    menu_manager = MenuManager()
    order_manager = OrderManager()

    while True:
        print("\n    RESTAURANTE   ")
        print("1. Gestión de Menús")
        print("2. Gestión de Órdenes")
        print("3. Salir")
        opcion_principal = input("Seleccione una opción: ")

        #* Opción 1: Gestión de Menús
        if opcion_principal == "1":
            while True:
                print("   GESTION MENU   \n1. Crear un nuevo menú\n2. Agregar ítem a un menú\n3. Ver ítems de un menú\n4. Actualizar un ítem en un menú\n5. Eliminar un ítem de un menú\n6. Volver al menú principal")
                opcion_menu = input("Seleccione una opción: ")
                if opcion_menu == "1":
                    menu_name = input("Ingrese el nombre del nuevo menú: ")
                    menu_manager.create_menu(menu_name)

                elif opcion_menu == "2":
                    menu_name = input("Ingrese el nombre del menú: ")
                    cantidad_items = int(input("Cantidad de ítems a agregar: "))
                    for _ in range(cantidad_items):
                        print("Seleccione el tipo de ítem: \n1. Bebida\n2. Plato Principal\n3. Entrada\n4. Postre")
                        
                        tipo = input("Opción: ")
                        name = input("Nombre del ítem: ")
                        price = float(input("Precio del ítem: "))

                        if tipo == "1":
                            size = input("Tamaño de la bebida (Normal/Grande/Pequeño): ")
                            item = Beverage(name=name, price=price, size=size)
                        elif tipo == "2":
                            protein = input("Tipo de proteína (Chicken/Beef/Seafood): ")
                            item = MainDish(name=name, price=price, protein_choice=protein)
                        elif tipo == "3":
                            extra = input("¿Porción extra? (Sí/No): ").lower() == "sí"
                            item = Starters(name=name, price=price, extra_portion=extra)
                        elif tipo == "4":
                            topping = input("Topping (Chocolate/Caramel/Nuts): ")
                            item = Desserts(name=name, price=price, topping=topping)
                        else:
                            print("Opción no válida.")
                            continue

                        menu_manager.add_item_to_menu(menu_name, item)

                elif opcion_menu == "3":
                    menu_name = input("Ingrese el nombre del menú: ")
                    menu_manager.show_menu(menu_name)

                elif opcion_menu == "4":
                    menu_name = input("Ingrese el nombre del menú: ")
                    menu_manager.show_menu(menu_name)
                    item_index = int(input("Índice del ítem a actualizar: "))

                    print("Seleccione el tipo de ítem:\n1. Bebida\n2. Plato Principal\n3. Entrada\n4. Postre")
                    tipo = input("Opción: ")

                    name = input("Nombre del ítem: ")
                    price = float(input("Precio del ítem: "))

                    if tipo == "1":
                        size = input("Tamaño de la bebida (Normal/Grande/Pequeño): ")
                        new_item = Beverage(name=name, price=price, size=size)
                    elif tipo == "2":
                        protein = input("Tipo de proteína (Chicken/Beef/Seafood): ")
                        new_item = MainDish(name=name, price=price, protein_choice=protein)
                    elif tipo == "3":
                        extra = input("¿Porción extra? (Sí/No): ").lower() == "sí"
                        new_item = Starters(name=name, price=price, extra_portion=extra)
                    elif tipo == "4":
                        topping = input("Topping (Chocolate/Caramel/Nuts): ")
                        new_item = Desserts(name=name, price=price, topping=topping)
                    else:
                        print("Opción no válida.")
                        continue

                    menu_manager.update_item_in_menu(menu_name, item_index, new_item)

                elif opcion_menu == "5":
                    menu_name = input("Ingrese el nombre del menú: ")
                    menu_manager.show_menu(menu_name)
                    item_index = int(input("Índice del ítem a eliminar: "))
                    menu_manager.delete_item_from_menu(menu_name, item_index)

                elif opcion_menu == "6":
                    break

                else:
                    print("Opción no válida. Intente de nuevo.")

        #* Opción 2: Gestión de Órdenes
        elif opcion_principal == "2":
            while True:
                print("\n   Gestión de Órdenes   \n1. Crear nueva orden\n2. Agregar ítem a la orden\n3. Ver ítems de la orden\n4. Ver total de la orden\n5. Procesar siguiente orden\n6. Ordenes en cola \n7. Volver al menú principal")

                opcion_orden = input("Seleccione una opción: ")

                if opcion_orden == "1":
                    order = Order()
                    order_manager.add_order(order)
                    print("Nueva orden creada.")

                elif opcion_orden == "2":
                    if order_manager.pending_orders() > 0:
                        menu_name = input("Ingrese el nombre del menú: ")
                        menu_manager.show_menu(menu_name)
                        item_index = int(input("Índice del ítem a agregar: "))

                        if menu_name in menu_manager.menu:
                            item_dict = menu_manager.menu[menu_name][item_index]
                            item = dict_to_item(item_dict)
                            order_manager.order_queue.queue[-1].add_item(item)
                            print(f"Ítem '{item.name}' agregado a la orden.")  # Corregido aquí
                        else:
                            print(f"El menú '{menu_name}' no existe.")
                    else:
                        print("No hay órdenes pendientes.")

                elif opcion_orden == "3":
                    if order_manager.pending_orders() > 0:
                        order = order_manager.order_queue.queue[-1]
                        print("Ítems en la orden:")
                        for item in order.items:
                            print(f"- {item}")
                    else:
                        print("No hay órdenes pendientes.")

                elif opcion_orden == "4":
                    if order_manager.pending_orders() > 0:
                        order = order_manager.order_queue.queue[-1]
                        total = order.calculate_total()
                        print(f"Total de la orden: ${total}")
                    else:
                        print("No hay órdenes pendientes.")

                elif opcion_orden == "5":
                    order_manager.process_next_order()
                    
                elif opcion_orden == "6":
                    if order_manager.pending_orders() > 0:
                        print("\n--- Órdenes en cola ---")
                        for index, order in enumerate(order_manager.order_queue.queue):
                            print(f"Orden {index + 1}:")
                            for item in order.items:
                                print(f"- {item}")
                            print(f"Total: ${order.calculate_total()}\n")
                    else:
                        print("No hay órdenes pendientes.")

                elif opcion_orden == "7":
                    break

                else:
                    print("Opción no válida. Intente de nuevo.")

        #* Opción 3: Salir
        elif opcion_principal == "3":
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()




