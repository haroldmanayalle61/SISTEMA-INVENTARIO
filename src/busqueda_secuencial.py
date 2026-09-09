from __future__ import annotations
#PARTE C
def busqueda_secuencial(self, codigo_buscado)->dict[str,bool|int]:
    comparaciones = 0
    # Recorremos el arreglo lineal de objetos Producto
    for i, producto in enumerate(self.productos):
        comparaciones += 1
        if producto.codigo == codigo_buscado:
            return {
                "encontrado": True, 
                "posicion": i, 
                "comparaciones": comparaciones
            }
    return {
        "encontrado": False, 
        "posicion": -1, 
        "comparaciones": comparaciones
    }
#REVISADO