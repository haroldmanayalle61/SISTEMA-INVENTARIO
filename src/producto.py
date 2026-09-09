class Producto:

    def __init__(self,codigo:int,nombre:str,categoria:str,precio_unitario:float,stock_actual:int):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio_unitario = precio_unitario
        self.stock_actual = stock_actual

    def __str__(self)->str:
        return (f"[{self.__codigo}] {self.__nombre} | Categoría: {self.__categoria} "
                f"| Precio: S/ {self.__precio_unitario:.2f} | Stock: {self.__stock_actual}")

 # GETTERS Y SETTERS 
    @property
    def codigo(self)->int:
        return self.__codigo
 
    @codigo.setter
    def codigo(self, nuevo_codigo)->None:
        if not isinstance(nuevo_codigo, int):
            raise ValueError("El código debe ser un número entero (int).")
        self.__codigo = nuevo_codigo
 
    @property
    def nombre(self)->str:
        return self.__nombre
 
    @nombre.setter
    def nombre(self, nuevo_nombre)->None:
        self.__nombre = nuevo_nombre
 
    @property
    def categoria(self)->str:
        return self.__categoria
 
    @categoria.setter
    def categoria(self, nueva_categoria)->None:
        self.__categoria = nueva_categoria
 
    @property
    def precio_unitario(self)->float:
        return self.__precio_unitario
 
    @precio_unitario.setter
    def precio_unitario(self, nuevo_precio)->None:
        if nuevo_precio < 0:
            raise ValueError("El precio unitario no puede ser negativo.")
        self.__precio_unitario = nuevo_precio
 
    @property
    def stock_actual(self)->int:
        return self.__stock_actual
 
    @stock_actual.setter
    def stock_actual(self, nuevo_stock)->None:
        if nuevo_stock < 0:
            raise ValueError("El stock actual no puede ser negativo.")
        self.__stock_actual = nuevo_stock
