from __future__ import annotations
from producto import Producto
from busqueda_secuencial import busqueda_secuencial as _busqueda_secuencial
from busqueda_binaria import busqueda_binaria as _busqueda_binaria
class Inventario:
    def __init__(self):
        # Atributo que almacena la colección de productos
        self.__productos = []

    # GETTERS Y SETTERS
    @property
    def productos(self)->list[Producto]:
        return self.__productos

    @productos.setter
    def productos(self, nueva_lista:list[Producto])->None:
        self.__productos = nueva_lista

    
    # MÉTODOS BASE 
    def registrar(self, producto:Producto)->None:
        """A1: Añade un producto al final del arreglo."""
        self.__productos.append(producto)

    def listar(self)->None:
        """A2: Muestra todos los productos registrados."""
        for producto in self.__productos:
            print(producto)

    def acceder(self, posicion:int)->Producto|None:
        """A3: Retorna un producto según su índice en el arreglo."""
        if 0 <= posicion < len(self.__productos):
            return self.__productos[posicion]
        return None

    def contar(self)->int:
        """A7: Retorna la cantidad actual de productos."""
        return len(self.__productos)

    # PARTE A - MÉTODOS DE FERNANDO
    def insertar(self, posicion:int, producto:Producto)->None:
        """A4: Inserta un producto en una posición indicada por el usuario."""

        if posicion < 0 or posicion > len(self.__productos):
            return False

        self.__productos.append(None)

        for i in range(len(self.__productos)-1, posicion, -1):
            self.__productos[i] = self.__productos[i-1]

        self.__productos[posicion] = producto

        return True
        

    def modificar(self, posicion:int, producto:Producto)->bool:
        """A5: Modifica el precio y stock de un producto buscando por su código."""

        if posicion < 0 or posicion >= len(self.__productos):
            return False

        self.__productos[posicion] = producto

        return True

    def eliminar(self, posicion:int)->bool:
        """A6: Elimina un producto según su código."""

        if posicion < 0 or posicion >= len(self.__productos):
            return False

        for i in range(posicion, len(self.__productos)-1):
            self.__productos[i] = self.__productos[i+1]

        self.__productos.pop()

        return True
        

    def ordenar_por_codigo(self)->None:
        # Ordenar la lista de productos por código usando el método sort() y una función lambda
        self.__productos.sort(key=lambda p: p.codigo)

    def codigo_existe(self, codigo:int)->bool:
        """Verifica si un código ya existe en el inventario."""
        return any(producto.codigo == codigo for producto in self.__productos)

    def busqueda_secuencial(self, codigo:int)->dict[str,bool|int]:
        return _busqueda_secuencial(self, codigo)

    def busqueda_binaria(self, codigo:int)->dict[str,bool|int]:
        return _busqueda_binaria(self, codigo)
#REVISADO