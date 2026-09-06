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
        if 0 <= posicion <= len(self._productos):
            self._productos.insert(posicion, producto)
            # Coordinación con Carlos (Parte D): Mantener ordenado por código
            self.ordenar_por_codigo()
            print("Producto insertado correctamente.")
        else:
            print("Error: Posición fuera de rango.")

    def modificar(self, codigo, nuevo_precio, nuevo_stock):
        """A5: Modifica el precio y stock de un producto buscando por su código."""
        for producto in self._productos:
            if producto.codigo == codigo: # Asume que Harold creó el atributo 'codigo'
                producto.precio_unitario = nuevo_precio
                producto.stock_actual = nuevo_stock
                print(f"Producto {codigo} modificado con éxito.")
                return True
        print("Error: Producto no encontrado para modificar.")
        return False

    def eliminar(self, codigo):
        """A6: Elimina un producto según su código."""
        for i in range(len(self._productos)):
            if self._productos[i].codigo == codigo:
                eliminado = self._productos.pop(i)
                print(f"Producto {eliminado.codigo} eliminado del inventario.")
                return True
        print("Error: Producto no encontrado para eliminar.")
        return False

    def ordenar_por_codigo(self):
        """Método de apoyo para garantizar que la búsqueda binaria de Carlos funcione."""
        # Ordena la lista basándose en el atributo 'codigo' de cada objeto Producto
        self._productos.sort(key=lambda p: p.codigo)
