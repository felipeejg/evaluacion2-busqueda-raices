import os
import csv
import numpy as np
from funciones import obtener_catalogo_funciones
from metodos import (
    biseccion,
    falsa_posicion,
    punto_fijo,
    secante,
    newton_raphson,
    newton_modificado
)

TOL = 1e-6
MAX_ITER = 100

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)


def exportar_csv_funcion(func_info):
    #genera el CSV con columnas (x, f(x)) en el intervalo [a, b].
    a, b = func_info["intervalo"]
    x_vals = np.linspace(a, b, 200)
    y_vals = func_info["f"](x_vals)
    
    ruta_csv = os.path.join(DATA_DIR, f"datos_{func_info['id']}.csv")
    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["x", "f(x)"])
        for x, y in zip(x_vals, y_vals):
            writer.writerow([f"{x:.8f}", f"{y:.8f}"])


def exportar_historial_pasos(func_id, resultados):
    #guarda el historial de iteraciones por método para graficar la convergencia.
    ruta_historial = os.path.join(DATA_DIR, f"pasos_{func_id}.csv")
    with open(ruta_historial, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Metodo", "Iteracion", "x_n", "abs_fx", "error_paso"])
        for nombre_metodo, res in resultados.items():
            for paso in res["pasos"]:
                n, x_val, abs_fx, err = paso
                writer.writerow([nombre_metodo, n, f"{x_val:.10f}", f"{abs_fx:.2e}", f"{err:.2e}"])


def main():
    catalogo = obtener_catalogo_funciones()
    filas_resumen_csv = []
    
    for func_info in catalogo:
        f = func_info["f"]
        df = func_info["df"]
        d2f = func_info["d2f"]
        g = func_info["g"]
        a, b = func_info["intervalo"]
        x0, x1 = func_info["x0"], func_info["x1"]
        
        #exportar datos de la curva (x, f(x))
        exportar_csv_funcion(func_info)
        
        #ejecutar los seis métodos numéricos
        resultados = {
            "Bisección": biseccion(f, a, b, TOL, MAX_ITER),
            "Falsa Posición": falsa_posicion(f, a, b, TOL, MAX_ITER),
            "Punto Fijo": punto_fijo(f, g, x0, TOL, MAX_ITER),
            "Secante": secante(f, x0, x1, TOL, MAX_ITER),
            "Newton-Raphson": newton_raphson(f, df, x0, TOL, MAX_ITER),
            "Newton Mejorado": newton_modificado(f, df, d2f, x0, TOL, MAX_ITER)
        }
        
        #exportar historial de pasos por función
        exportar_historial_pasos(func_info["id"], resultados)
        
        print(f"\nFunción: {func_info['categoria']} -> {func_info['nombre_corto']}")
        for nombre_m, res in resultados.items():
            error_real = abs(res["raiz"] - func_info["raiz_exacta"]) if not np.isnan(res["raiz"]) else np.nan
            filas_resumen_csv.append([
                func_info["categoria"],
                func_info["nombre_corto"],
                nombre_m,
                "Si" if res["convergio"] else "No",
                res["iteraciones"],
                f"{res['raiz']:.8f}" if not np.isnan(res["raiz"]) else "NaN",
                f"{res['error']:.2e}" if not np.isnan(res["error"]) else "NaN",
                f"{error_real:.2e}" if not np.isnan(error_real) else "NaN",
                res["motivo"]
            ])
            estado_str = f"Raíz = {res['raiz']:.6f} ({res['iteraciones']} iter)" if res["convergio"] else f"FALLÓ ({res['motivo']})"
            print(f"  - {nombre_m:16s}: {estado_str}")
            
    # guardar archivo CSV consolidado de convergencia
    ruta_resumen = os.path.join(DATA_DIR, "resumen_convergencia.csv")
    with open(ruta_resumen, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Categoria", "Funcion", "Metodo", "Convergio", "Iteraciones", "Raiz_Aproximada", "Error_Paso", "Error_Real", "Observacion"])
        writer.writerows(filas_resumen_csv)

if __name__ == "__main__":
    main()