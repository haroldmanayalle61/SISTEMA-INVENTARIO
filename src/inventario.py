from __future__ import annotations
from producto import Producto

class Inventario:
    def __init__(self,productos:list[Producto]):
        # Atributo que almacena la colección de productos
        self._productos = []

    # GETTERS Y SETTERS
    @property
    def productos(self)->list[Producto]:
        return self._productos

    @productos.setter
    def productos(self, nueva_lista:list[Producto])->None:
        self._productos = nueva_lista

    
    # MÉTODOS BASE 
    def registrar(self, producto:Producto)->None:
        """A1: Añade un producto al final del arreglo."""
        self._productos.append(producto)

    def listar(self)->None:
        """A2: Muestra todos los productos registrados."""
        for producto in self._productos:
            print(producto)

    def acceder(self, posicion:int)->Producto|None:
        """A3: Retorna un producto según su índice en el arreglo."""
        if 0 <= posicion < len(self._productos):
            return self._productos[posicion]
        return None

    def contar(self)->int:
        """A7: Retorna la cantidad actual de productos."""
        return len(self._productos)

    # PARTE A - MÉTODOS DE FERNANDO
    def insertar(self, posicion:int, producto:int)->None:
        """A4: Inserta un producto en una posición indicada por el usuario."""
        if 0 <= posicion <= len(self._productos):
            self._productos.insert(posicion, producto)
            # Coordinación con Carlos (Parte D): Mantener ordenado por código
            self.ordenar_por_codigo()
            print("Producto insertado correctamente.")
        else:
            print("Error: Posición fuera de rango.")

    def modificar(self, codigo:int, nuevo_precio:float, nuevo_stock:int)->bool:
        """A5: Modifica el precio y stock de un producto buscando por su código."""
        for producto in self._productos:
            if producto.codigo == codigo:
                producto.precio_unitario = nuevo_precio
                producto.stock_actual = nuevo_stock
                print(f"Producto {codigo} modificado con éxito.")
                return True
        print("Error: Producto no encontrado para modificar.")
        return False

    def eliminar(self, codigo:int)->None:
        """A6: Elimina un producto según su código."""
        for i in range(len(self._productos)):
            if self._productos[i].codigo == codigo:
                eliminado = self._productos.pop(i)
                print(f"Producto {eliminado.codigo} eliminado del inventario.")
                return True
        print("Error: Producto no encontrado para eliminar.")
        return False

    def ordenar_por_codigo(self)->None:
        """Método de apoyo para garantizar que la búsqueda binaria de Carlos funcione."""
        # Ordena la lista basándose en el atributo 'codigo' de cada objeto Producto
        self._productos.sort(key=lambda p: p.codigo)#lambda (función extractora del codigo)

    def codigo_existe(self, codigo:int)->bool:
        """Verifica si un código ya existe en el inventario."""
        return any(producto.codigo == codigo for producto in self._productos)
#REVISADO