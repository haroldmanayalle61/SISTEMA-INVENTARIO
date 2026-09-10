from __future__ import annotations
#PARTE D

def busqueda_binaria(self, codigo_buscado:int)->dict[str,bool|int]:
    """
    Busqueda binaria manual sobre self.__productos. 
    Se debe llamar a ordenar_por_codigo() en el main antes de 
    usar este método para garantizar que la lista esté ordenada.
    """
    comparaciones = 0
    limite_inferior = 0
    limite_superior = len(self.productos) - 1

    while limite_inferior <= limite_superior:
        posicion_central = (limite_inferior + limite_superior) // 2
        comparaciones += 1
        elemento_central = self.productos[posicion_central]

        if elemento_central.codigo == codigo_buscado:
            return {
                "encontrado": True,
                "posicion": posicion_central,
                "comparaciones": comparaciones
            }
        elif elemento_central.codigo < codigo_buscado:
            limite_inferior = posicion_central + 1
        else:
            limite_superior = posicion_central - 1

    return {
        "encontrado": False,
        "posicion": -1,
        "comparaciones": comparaciones
    }
#REVISADO