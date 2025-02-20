from Restaurante.Menu import *
from queue import Queue

#* Clase para instaciar ordenes
class Order:
    def __init__(self):
        self.items = []


    #* Agregar un ítem a la orden
    def add_item(self, item):
        if isinstance(item, MenuItem):
            self.items.append(item.to_tuple())
        else:
            raise ValueError("El ítem debe ser una instancia de MenuItem o sus subclases")
    #* Calcular el total de la orden
    def calculate_total(self):
        return sum(item.price for item in self.items)

    
#* Clase para manejar las ordenes que entren 
class OrderManager:
    def __init__(self):
        self.order_queue = Queue()

    #* Agregar una orden a la cola
    def add_order(self, order):
        if isinstance(order, Order):
            self.order_queue.put(order)
            print(f"Orden agregada: {order.items}")
        else:
            raise ValueError("Solo se pueden agregar instancias de Order")

    #* Procesar la siguiente orden en la cola
    def process_next_order(self):
        #? FIFO
        if not self.order_queue.empty():
            next_order = self.order_queue.get()
            total = next_order.calculate_total()
            print(f"Procesando orden: {next_order.items}")
            print(f"Total a pagar: {total}")
            return next_order
        else:
            print("No hay órdenes pendientes.")
            return None
        
        
    #* Ver la cantidad de ordenes pendientes
    def pending_orders(self):
        return self.order_queue.qsize()

