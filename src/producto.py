class Producto:

    def __init__(self,codigo:int,nombre:str,categoria:str,precio_unitario:float,stock_actual:int):
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio_unitario = precio_unitario
        self._stock_actual = stock_actual

    def __str__(self):
        return (f"[{self._codigo}] {self._nombre} | Categoría: {self._categoria} "
                f"| Precio: S/ {self._precio_unitario:.2f} | Stock: {self._stock_actual}")

 # GETTERS Y SETTERS 
    @property
    def codigo(self):
        return self._codigo
 
    @codigo.setter
    def codigo(self, nuevo_codigo):
        if not isinstance(nuevo_codigo, int):
            raise ValueError("El código debe ser un número entero (int).")
        self._codigo = nuevo_codigo
 
    @property
    def nombre(self):
        return self._nombre
 
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
 
    @property
    def categoria(self):
        return self._categoria
 
    @categoria.setter
    def categoria(self, nueva_categoria):
        self._categoria = nueva_categoria
 
    @property
    def precio_unitario(self):
        return self._precio_unitario
 
    @precio_unitario.setter
    def precio_unitario(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio unitario no puede ser negativo.")
        self._precio_unitario = nuevo_precio
 
    @property
    def stock_actual(self):
        return self._stock_actual
 
    @stock_actual.setter
    def stock_actual(self, nuevo_stock):
        if nuevo_stock < 0:
            raise ValueError("El stock actual no puede ser negativo.")
        self._stock_actual = nuevo_stock
 