class Producto:

    def __init__(self,codigo:int,nombre:str,categoria:str,precio_unitario:float,stock_actual:int):
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio_unitario = precio_unitario
        self._stock_actual = stock_actual

    def __str__(self)->None:
        return (f"[{self._codigo}] {self._nombre} | Categoría: {self._categoria} "
                f"| Precio: S/ {self._precio_unitario:.2f} | Stock: {self._stock_actual}")

 # GETTERS Y SETTERS 
    @property
    def codigo(self)->int:
        return self._codigo
 
    @codigo.setter
    def codigo(self, nuevo_codigo)->None:
        if not isinstance(nuevo_codigo, int):
            raise ValueError("El código debe ser un número entero (int).")
        self._codigo = nuevo_codigo
 
    @property
    def nombre(self)->str:
        return self._nombre
 
    @nombre.setter
    def nombre(self, nuevo_nombre)->None:
        self._nombre = nuevo_nombre
 
    @property
    def categoria(self)->str:
        return self._categoria
 
    @categoria.setter
    def categoria(self, nueva_categoria)->None:
        self._categoria = nueva_categoria
 
    @property
    def precio_unitario(self)->float:
        return self._precio_unitario
 
    @precio_unitario.setter
    def precio_unitario(self, nuevo_precio)->None:
        if nuevo_precio < 0:
            raise ValueError("El precio unitario no puede ser negativo.")
        self._precio_unitario = nuevo_precio
 
    @property
    def stock_actual(self)->int:
        return self._stock_actual
 
    @stock_actual.setter
    def stock_actual(self, nuevo_stock)->None:
        if nuevo_stock < 0:
            raise ValueError("El stock actual no puede ser negativo.")
        self._stock_actual = nuevo_stock

 #ARREGLAR LO DEL INMUNDO , INSERTAR POR POSICION