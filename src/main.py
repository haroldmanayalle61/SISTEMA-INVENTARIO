#MENU-INTERFAZ
"""
Integra en un solo flujo:
    - Clases base: Producto, Inventario                (Harold)
    - Parte A: Arreglo lineal / CRUD                    (Fernando)
    - Parte B: Arreglo bidimensional (matriz de stock)   (Diego)
    - Parte C: Busqueda secuencial                       (Marciano)
    - Parte D: Busqueda binaria                          (Carlos)
    - Parte E: Pruebas experimentales de eficiencia      (FernanLR)
"""

from producto import Producto
from inventario import Inventario
import matriz_stock as ms
import pruebas_eficiencia as pe

NUM_ALMACENES = 3

# DATOS DE DEMOSTRACION
def leer_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print("Error: debe ingresar un numero entero.")
        return None


def leer_flotante(mensaje):
    try:
        return float(input(mensaje))
    except ValueError:
        print("Error: debe ingresar un numero valido.")
        return None



# SUBMENU: ARREGLO LINEAL (Parte A)
def menu_arreglo_lineal(inventario):
    while True:
        print("\n--- ARREGLO LINEAL (Producto / Inventario) ---")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Acceder por posicion")
        print("4. Insertar en una posicion")
        print("5. Modificar producto (por codigo)")
        print("6. Eliminar producto (por codigo)")
        print("7. Contar productos")
        print("0. Volver al menu principal")
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            codigo = leer_entero("Codigo: ")
            if codigo is None:
                continue
            if inventario.codigo_existe(codigo):
                print("Error: el codigo ya existe en el inventario.")
                continue
            nombre = input("Nombre: ")
            categoria = input("Categoria: ")
            precio = leer_flotante("Precio unitario: ")
            stock = leer_entero("Stock actual: ")
            if precio is None or stock is None:
                continue
            try:
                inventario.registrar(Producto(codigo, nombre, categoria, precio, stock))
                print("Producto registrado.")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "2":
            if inventario.contar() == 0:
                print("El inventario esta vacio.")
            inventario.listar()

        elif opcion == "3":
            posicion = leer_entero("Posicion a consultar: ")
            if posicion is None:
                continue
            producto = inventario.acceder(posicion)
            print(producto if producto else "Error: posicion fuera de rango.")

        elif opcion == "4":
            posicion = leer_entero("Posicion donde insertar: ")
            if posicion is None:
                continue
            while True:    
                codigo = leer_entero("Codigo: ")
                if inventario.codigo_existe(codigo):
                    print("Error: el codigo ya existe en el inventario. Ingresa otro.")
                else:
                    break
            nombre = input("Nombre: ")
            categoria = input("Categoria: ")
            precio = leer_flotante("Precio unitario: ")
            stock = leer_entero("Stock actual: ")
            if None in (codigo, precio, stock):
                continue
            inventario.insertar(posicion, Producto(codigo, nombre, categoria, precio, stock))

        elif opcion == "5":
            codigo = leer_entero("Codigo del producto a modificar: ")
            if codigo is None:
                continue
            precio = leer_flotante("Nuevo precio: ")
            stock = leer_entero("Nuevo stock: ")
            if precio is None or stock is None:
                continue
            inventario.modificar(codigo, precio, stock)

        elif opcion == "6":
            codigo = leer_entero("Codigo del producto a eliminar: ")
            if codigo is None:
                continue
            inventario.eliminar(codigo)

        elif opcion == "7":
            print(f"Total de productos: {inventario.contar()}")

        elif opcion == "0":
            return
        else:
            print("Opcion invalida.")

# SUBMENU: ARREGLO BIDIMENSIONAL (Parte B)
def menu_matriz_stock(inventario, estado):
    while True:
        print("\n--- MATRIZ DE STOCK (arreglo bidimensional) ---")
        print("1. Generar matriz a partir del inventario actual")
        print("2. Mostrar matriz completa")
        print("3. Acceder a una posicion (fila, columna)")
        print("4. Modificar stock de una posicion")
        print("5. Recorrer por filas")
        print("6. Recorrer por columnas")
        print("7. Stock total por producto")
        print("8. Stock total por almacen")
        print("0. Volver al menu principal")
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            if inventario.contar() == 0:
                print("Primero registra productos en el arreglo lineal.")
                continue
            estado["matriz"] = ms.generar_matriz(inventario, NUM_ALMACENES)
            print("Matriz generada a partir del inventario.")

        elif opcion in ("2", "3", "4", "5", "6", "7", "8") and estado["matriz"] is None:
            print("Primero genera la matriz (opcion 1).")

        elif opcion == "2":
            ms.mostrar_matriz(estado["matriz"])

        elif opcion == "3":
            fila = leer_entero("Fila (1..n, producto): ")
            columna = leer_entero("Columna (1..n, almacen): ")
            if fila is None or columna is None:
                continue
            valor = ms.acceder_posicion(estado["matriz"], fila, columna)
            if valor is not None:
                print(f"Stock en ({fila},{columna}): {valor}")

        elif opcion == "4":
            fila = leer_entero("Fila: ")
            columna = leer_entero("Columna: ")
            nuevo = leer_entero("Nuevo stock: ")
            if None in (fila, columna, nuevo):
                continue
            ms.modificar_stock_posicion(estado["matriz"], fila, columna, nuevo, inventario)

        elif opcion == "5":
            ms.recorrer_por_filas(estado["matriz"])

        elif opcion == "6":
            ms.recorrer_por_columnas(estado["matriz"])

        elif opcion == "7":
            print(ms.stock_total_por_producto(estado["matriz"]))

        elif opcion == "8":
            print(ms.stock_total_por_almacen(estado["matriz"]))

        elif opcion == "0":
            return
        else:
            print("Opcion invalida.")


# SUBMENU: BUSQUEDAS (Partes C y D)
def menu_busquedas(inventario):
    while True:
        print("\n--- BUSQUEDAS ---")
        print("1. Busqueda secuencial")
        print("2. Busqueda binaria (requiere datos ordenados por codigo)")
        print("0. Volver al menu principal")
        opcion = input("Elige una opcion: ").strip()

        if opcion in ("1", "2"):
            codigo = leer_entero("Codigo a buscar: ")
            if codigo is None:
                continue
            if opcion == "1":
                resultado = inventario.busqueda_secuencial(codigo)
                nombre_algoritmo = "Secuencial"
            else:
                inventario.ordenar_por_codigo()
                resultado = inventario.busqueda_binaria(codigo)
                nombre_algoritmo = "Binaria"

            print(f"\nAlgoritmo: {nombre_algoritmo}")
            print(f"Encontrado: {resultado['encontrado']}")
            print(f"Posicion: {resultado['posicion']}")
            print(f"Comparaciones realizadas: {resultado['comparaciones']}")

        elif opcion == "0":
            return
        else:
            print("Opcion invalida.")


# SUBMENU: PRUEBAS DE EFICIENCIA (Parte E)
def menu_pruebas_eficiencia():
    print("\n--- PRUEBAS EXPERIMENTALES DE EFICIENCIA ---")
    print("Se generaran inventarios de 100, 1 000, 10 000 y 100 000 productos")
    print("y se compararan ambos algoritmos de busqueda. Esto puede tardar unos segundos...\n")
    resultados = pe.ejecutar_experimentos()
    pe.imprimir_tabla_resultados(resultados)
    pe.exportar_a_csv(resultados)


# MENU PRINCIPAL
def menu_principal():
    inventario = Inventario()
    estado = {"matriz": None}

    print("=== SISTEMA DE GESTION DE INVENTARIO ===")
    print("El inventario empieza vacio. Usa la opcion 1 para registrar productos.")

    while True:
        print("\n===================== MENU PRINCIPAL =====================")
        print("1. Arreglo lineal (CRUD de productos)")
        print("2. Arreglo bidimensional (matriz de stock)")
        print("3. Busquedas (secuencial y binaria)")
        print("4. Pruebas experimentales de eficiencia")
        print("0. Salir")
        print("============================================================")
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            menu_arreglo_lineal(inventario)
        elif opcion == "2":
            menu_matriz_stock(inventario, estado)
        elif opcion == "3":
            menu_busquedas(inventario)
        elif opcion == "4":
            menu_pruebas_eficiencia()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    menu_principal()