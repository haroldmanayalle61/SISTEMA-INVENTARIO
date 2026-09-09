# PARTE E - Pruebas experimentales de eficiencia

import time
import random

from producto import Producto
from inventario import Inventario

def generar_inventario_prueba(cantidad):
    # Crea un inventario con "cantidad" productos, codigos de 0 a cantidad-1
    categorias = ["Abarrotes", "Limpieza", "Electronica", "Ferreteria", "Papeleria"]
    inventario = Inventario()#equivalente en java a Inventario inventario = new Inventario();
    for codigo in range(cantidad):
        nombre = "Producto" + str(codigo)
        categoria = random.choice(categorias)
        precio = round(random.uniform(1.0, 500.0), 2)
        stock = random.randint(0, 200)
        producto = Producto(codigo, nombre, categoria, precio, stock)
        inventario.registrar(producto)
    inventario.ordenar_por_codigo()
    return inventario


def obtener_codigos_prueba(cantidad):
    # Los 4 casos minimos: inicio, centro, final e inexistente
    inicio = 0
    centro = cantidad // 2
    final = cantidad - 1
    inexistente = cantidad + 999999
    return [
        ("inicio", inicio),
        ("centro", centro),
        ("final", final),
        ("inexistente", inexistente),
    ]


def medir_tiempo(funcion_busqueda, codigo):
    inicio_tiempo = time.perf_counter()
    resultado = funcion_busqueda(codigo)
    fin_tiempo = time.perf_counter()
    tiempo_usado = fin_tiempo - inicio_tiempo
    return resultado, tiempo_usado


def ejecutar_experimentos():
    tamanos = [100, 1000, 10000, 100000]
    resultados = []

    for tamano in tamanos:
        inventario = generar_inventario_prueba(tamano)
        codigos_prueba = obtener_codigos_prueba(tamano)

        for condicion, codigo in codigos_prueba:
            # Probamos primero secuencial y luego binaria con el mismo codigo
            resultado_sec, tiempo_sec = medir_tiempo(inventario.busqueda_secuencial, codigo)
            resultados.append({
                "tamano_n": tamano,
                "algoritmo": "Secuencial",
                "condicion": condicion,
                "codigo_buscado": codigo,
                "encontrado": resultado_sec["encontrado"],
                "posicion": resultado_sec["posicion"],
                "comparaciones": resultado_sec["comparaciones"],
                "tiempo_segundos": tiempo_sec,
            })

            resultado_bin, tiempo_bin = medir_tiempo(inventario.busqueda_binaria, codigo)
            resultados.append({
                "tamano_n": tamano,
                "algoritmo": "Binaria",
                "condicion": condicion,
                "codigo_buscado": codigo,
                "encontrado": resultado_bin["encontrado"],
                "posicion": resultado_bin["posicion"],
                "comparaciones": resultado_bin["comparaciones"],
                "tiempo_segundos": tiempo_bin,
            })

    return resultados


def imprimir_tabla_resultados(resultados):
    print(f"{'n':>8} | {'Algoritmo':<10} | {'Condicion':<11} | {'Codigo':>10} | "
          f"{'Encontrado':<10} | {'Posicion':>8} | {'Comparaciones':>13} | {'Tiempo (s)':>12}")
    print("-" * 100)
    for r in resultados:
        print(f"{r['tamano_n']:>8} | {r['algoritmo']:<10} | {r['condicion']:<11} | "
              f"{r['codigo_buscado']:>10} | {str(r['encontrado']):<10} | "
              f"{r['posicion']:>8} | {r['comparaciones']:>13} | {r['tiempo_segundos']:.8f}")


def exportar_a_csv(resultados, ruta_archivo="resultados_eficiencia.csv"):
    archivo = open(ruta_archivo, "w", encoding="utf-8")
    archivo.write("tamano_n,algoritmo,condicion,codigo_buscado,encontrado,posicion,comparaciones,tiempo_segundos\n")
    for r in resultados:
        linea = f"{r['tamano_n']},{r['algoritmo']},{r['condicion']},{r['codigo_buscado']}," \
                f"{r['encontrado']},{r['posicion']},{r['comparaciones']},{r['tiempo_segundos']}\n"
        archivo.write(linea)
    archivo.close()
    print("\nResultados exportados a:", ruta_archivo)


if __name__ == "__main__":
    print("=== PARTE E: Pruebas experimentales de eficiencia ===\n")
    resultados = ejecutar_experimentos()
    imprimir_tabla_resultados(resultados)
    exportar_a_csv(resultados)