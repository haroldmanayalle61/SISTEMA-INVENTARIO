from __future__ import annotations
import random
from inventario import Inventario
#PARTE B - ARREGLO BIDIMENSIONAL (MATRIZ DE STOCK)

def generar_encabezado(num_almacenes: int) -> list[str]:
    """Construye la fila de encabezado con el nombre de cada almacén."""
    encabezado = ["Producto"]
    for i in range(1, num_almacenes + 1):
        encabezado.append(f"Almacen {i}")
    return encabezado


def _repartir_stock(stock_total: int, num_almacenes: int) -> list[int]:
    """Reparte aleatoriamente el stock total de un producto entre los almacenes,
    de modo que la suma de los valores generados sea igual al stock_total.."""
    if num_almacenes <= 0:
        return []

    valores_por_almacen = []
    stock_restante = stock_total

    for i in range(num_almacenes):
        es_el_ultimo_almacen = (i == num_almacenes - 1)
        if es_el_ultimo_almacen:
            valor_asignado = stock_restante
        else:
            valor_asignado = random.randint(0, stock_restante)

        valores_por_almacen.append(valor_asignado)
        stock_restante -= valor_asignado

    return valores_por_almacen


def registrar_fila(matriz: list[list], codigo: int, valores_almacenes: list[int]) -> bool:
    """B1: Registra en la matriz una nueva fila (producto) con su stock por almacén."""
    num_almacenes = len(matriz[0]) - 1
    if len(valores_almacenes) != num_almacenes:
        print(f"Error: se esperaban {num_almacenes} valores de almacén y se recibieron {len(valores_almacenes)}.")
        return False
    fila = [codigo] + list(valores_almacenes)
    matriz.append(fila)
    return True


def generar_matriz(inventario: Inventario, num_almacenes: int) -> list[list]:
    """B1: Genera la matriz completa de stock a partir de los productos ya
    registrados en el inventario, repartiendo el stock de cada uno entre
    los almacenes indicados."""
    matriz = [generar_encabezado(num_almacenes)]
    for i in range(inventario.contar()):
        producto = inventario.acceder(i)
        valores_almacenes = _repartir_stock(producto.stock_actual, num_almacenes)
        registrar_fila(matriz, producto.codigo, valores_almacenes)
    return matriz


def mostrar_matriz(matriz: list[list]) -> None:
    """B2: Muestra la matriz completa (encabezado y todas las filas de datos)."""
    for fila in matriz:
        for valor in fila:
            print(f"\t{valor}", end="")
        print()


def acceder_posicion(matriz: list[list], fila: int, columna: int) -> int | None:
    """B3: Accede al stock de una posición específica."""
    if 1 <= fila < len(matriz) and 1 <= columna < len(matriz[0]):
        return matriz[fila][columna]
    print("Error: las coordenadas ingresadas están fuera de rango.")
    return None


def _buscar_producto_por_codigo(inventario: Inventario, codigo: int):
    for i in range(inventario.contar()):
        producto = inventario.acceder(i)
        if producto.codigo == codigo:
            return producto
    return None


def modificar_stock_posicion(matriz: list[list], fila: int, columna: int, nuevo_stock: int, inventario: Inventario) -> bool:
    """B4: Modifica el stock de una posición específica (fila, columna) de la matriz."""
    if nuevo_stock < 0:
        print("Error: el stock no puede ser negativo.")
        return False
    if not (1 <= fila < len(matriz) and 1 <= columna < len(matriz[0])):
        print("Error: las coordenadas ingresadas están fuera de rango.")
        return False

    codigo_producto = matriz[fila][0]
    stock_anterior = matriz[fila][columna]

    producto = _buscar_producto_por_codigo(inventario, codigo_producto)
    if producto is None:
        print(f"Error: el producto {codigo_producto} no existe en el inventario.")
        return False

    diferencia = nuevo_stock - stock_anterior
    try:
        producto.stock_actual = producto.stock_actual + diferencia
    except ValueError as error:
        print(f"Error: no se pudo actualizar el stock del producto ({error}).")
        return False

    matriz[fila][columna] = nuevo_stock
    print(f"Stock modificado correctamente en la coordenada ({fila}, {columna}).")
    return True


def actualizar_stock_por_codigo(matriz: list[list], codigo: int, num_almacen: int, nuevo_stock: int, inventario: Inventario) -> bool:
    """modifica el stock de un producto identificándolo por su código"""
    if nuevo_stock < 0:
        print("Error: el stock no puede ser negativo.")
        return False
    if num_almacen < 1 or num_almacen >= len(matriz[0]):
        print("Error: el almacén indicado no existe.")
        return False

    for i in range(1, len(matriz)):
        if matriz[i][0] == codigo:
            stock_anterior = matriz[i][num_almacen] 
            producto = _buscar_producto_por_codigo(inventario, codigo)
            if producto is None:
                print(f"Error: el producto {codigo} no existe en el inventario.")
                return False

            diferencia = nuevo_stock - stock_anterior
            try:
                producto.stock_actual = producto.stock_actual + diferencia
            except ValueError as error:
                print(f"Error: no se pudo actualizar el stock del producto ({error}).")
                return False

            matriz[i][num_almacen] = nuevo_stock
            print(f"Stock del producto {codigo} actualizado a {nuevo_stock} en el Almacen {num_almacen}.")
            return True

    print(f"Error: el código {codigo} no se encuentra registrado en la matriz.")
    return False

def recorrer_por_filas(matriz: list[list]) -> None:
    """B5: Recorre la matriz fila por fila (producto por producto). Por cada
    producto, recorre sus columnas y muestra el stock en cada almacén."""
    encabezado = matriz[0]

    for i in range(1, len(matriz)):
        fila = matriz[i]
        codigo_producto = fila[0]
        print(f"Producto {codigo_producto}:", end=" ")

        for j in range(1, len(fila)):
            nombre_almacen = encabezado[j]
            stock = fila[j]
            print(f"{nombre_almacen}={stock}", end="  ")

        print() 

def recorrer_por_columnas(matriz: list[list]) -> None:
    """B6: Recorre la matriz columna por columna (almacén por almacén)"""
    encabezado = matriz[0]
    num_almacenes = len(encabezado) - 1

    for columna in range(1, num_almacenes + 1):
        nombre_almacen = encabezado[columna]
        print(f"{nombre_almacen}:", end=" ")

        for fila in range(1, len(matriz)):
            codigo_producto = matriz[fila][0]
            stock = matriz[fila][columna]
            print(f"P{codigo_producto}={stock}", end="  ")

        print() 

def stock_total_por_producto(matriz: list[list]) -> dict:
    """B7: Calcula el stock total de cada producto sumando su fila completa
    (todas las columnas de almacén). Recorrido O(n^2)."""
    totales = {}
    for i in range(1, len(matriz)):
        fila = matriz[i]
        totales[fila[0]] = sum(fila[1:])
    return totales

def stock_total_por_almacen(matriz: list[list]) -> dict:
    """B8: Calcula el stock total de cada almacén sumando su columna completa
    (todas las filas de productos). complejidad O(n^2)."""
    encabezado = matriz[0]
    num_almacenes = len(encabezado) - 1
    totales = {}
    for columna in range(1, num_almacenes + 1):
        total_columna = 0
        for fila in range(1, len(matriz)):
            total_columna += matriz[fila][columna]
        totales[encabezado[columna]] = total_columna
    return totales