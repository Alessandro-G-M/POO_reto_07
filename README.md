# POO_reto_07 Restaurante - Gestión de Menús y Órdenes

Este proyecto es una solución a un reto de programación orientada a objetos que consiste en la gestión de menús y órdenes en un restaurante. El sistema permite crear, actualizar, eliminar y visualizar ítems en diferentes menús, así como gestionar órdenes utilizando una cola FIFO (First In, First Out).

## Estructura del Reto

El reto está organizado en los siguientes archivos:

- **`main.py`**: Punto de entrada del programa. Contiene el menú principal y la lógica para interactuar con las clases de gestión de menús y órdenes.
- **`Restaurante/Menu.py`**: Define las clases para los ítems del menú (`Beverage`, `MainDish`, `Starters`, `Desserts`) y una clase base `MenuItem`. También incluye un `namedtuple` para representar los ítems del menú.
- **`Restaurante/Menu_Manager.py`**: Contiene la clase `MenuManager` que gestiona la creación, actualización, eliminación y visualización de menús. Los menús se almacenan en un archivo JSON.
- **`Restaurante/Order_Manager.py`**: Contiene las clases `Order` y `OrderManager`. `Order` representa una orden con ítems, y `OrderManager` gestiona una cola de órdenes utilizando una estructura FIFO.
- **`Restaurante/__init__.py`**: Archivo de inicialización del paquete `Restaurante`.

## Funcionalidades

### Gestión de Menús

1. **Crear un nuevo menú**: Permite crear un nuevo menú con un nombre específico.
2. **Agregar ítem a un menú**: Permite agregar ítems de diferentes tipos (bebidas, platos principales, entradas, postres) a un menú existente.
3. **Ver ítems de un menú**: Muestra todos los ítems de un menú específico.
4. **Actualizar un ítem en un menú**: Permite modificar un ítem existente en un menú.
5. **Eliminar un ítem de un menú**: Permite eliminar un ítem de un menú.

### Gestión de Órdenes

1. **Crear nueva orden**: Crea una nueva orden vacía.
2. **Agregar ítem a la orden**: Permite agregar ítems de un menú a una orden existente.
3. **Ver ítems de la orden**: Muestra todos los ítems de una orden específica.
4. **Ver total de la orden**: Calcula y muestra el total a pagar de una orden.
5. **Procesar siguiente orden**: Procesa la siguiente orden en la cola (FIFO) y muestra el total a pagar.
6. **Ver órdenes en cola**: Muestra todas las órdenes pendientes en la cola.

## Ejecución del Programa

Para ejecutar el programa, simplemente ejecuta el archivo `main.py`:

```bash
python main.py
