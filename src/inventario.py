class Inventario:
    def __init__(self):
        # Atributo que almacena la colección de productos
        self._productos = []

    # GETTERS Y SETTERS
    def get_productos(self):
        return self._productos

    def set_productos(self, nueva_lista):
        self._productos = nueva_lista

    
    # MÉTODOS BASE 
    def registrar(self, producto):
        """A1: Añade un producto al final del arreglo."""
        self._productos.append(producto)

    def listar(self):
        """A2: Muestra todos los productos registrados."""
        for producto in self._productos:
            print(producto)

    def acceder(self, posicion):
        """A3: Retorna un producto según su índice en el arreglo."""
        if 0 <= posicion < len(self._productos):
            return self._productos[posicion]
        return None

    def contar(self):
        """A7: Retorna la cantidad actual de productos."""
        return len(self._productos)

    # PARTE A - MÉTODOS DE FERNANDO
    def insertar(self, posicion, producto):
        """A4: Inserta un producto en una posición indicada por el usuario."""
        pass

    def modificar(self, codigo, nuevos_datos):
        """A5: Modifica los datos de un producto existente."""
        pass

    def eliminar(self, codigo):
        """A6: Elimina un producto según su código."""
        pass
