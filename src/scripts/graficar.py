import os
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from funciones import obtener_catalogo_funciones

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)


def graficar_funcion_con_raiz(func_info):
    #lee el CSV de la función y genera el gráfico con la raíz marcada.
    nombre_seguro = func_info["id"].strip().replace(" ", "_").lower()
    ruta_csv = os.path.join(DATA_DIR, f"datos_{nombre_seguro}.csv")
    if not os.path.exists(ruta_csv):
        print(f"Advertencia: No se encontró {ruta_csv}")
        return
        
    x_vals, y_vals = [], []
    with open(ruta_csv, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for fila in reader:
            x_vals.append(float(fila[0]))
            y_vals.append(float(fila[1]))
            
    a, b = func_info["intervalo"]
    raiz = func_info["raiz_exacta"]
    f_obj = func_info["f"]
    
    plt.figure(figsize=(8, 5), dpi=150)
    plt.axhline(0, color="black", linewidth=1.2, linestyle="--", label="Eje y = 0")
    plt.plot(x_vals, y_vals, color="#1f77b4", linewidth=2.5, label=func_info["expresion_latex"])
    
    if func_info["tipo_raiz"] == "simple":
        plt.scatter([a, b], [f_obj(a), f_obj(b)], color="#ff7f0e", s=70, zorder=5,
                    label=f"Extremos: f({a})={f_obj(a):.2f}, f({b})={f_obj(b):.2f} (Bolzano < 0)")
    else:
        plt.annotate("Tangencia al eje x\n(Sin cambio de signo: f(x) >= 0)",
                     xy=(raiz, 0), xytext=(raiz - 0.5, 0.4),
                     arrowprops=dict(facecolor="red", shrink=0.08, width=1.5, headwidth=6),
                     fontsize=9, fontweight="bold", color="#d62728")
        
    plt.scatter([raiz], [f_obj(raiz)], color="#d62728", s=100, zorder=6,
                label=f"Raíz x* ≈ {raiz:.6f}")
    
    plt.title(f"Ambiente Controlado: {func_info['categoria']} - {func_info['nombre_corto']}", fontsize=12, fontweight="bold")
    plt.xlabel("x", fontsize=11)
    plt.ylabel("f(x)", fontsize=11)
    plt.grid(True, linestyle=":", alpha=0.7)
    plt.legend(loc="best", fontsize=9)
    plt.tight_layout()
    
    ruta_guardado = os.path.join(ASSETS_DIR, f"funcion_{nombre_seguro}.png")
    plt.savefig(ruta_guardado)
    plt.close()


def graficar_convergencia(func_info):
    #lee el archivo de pasos y grafica |error| vs iteración en escala semilogarítmica.
    nombre_seguro = func_info["id"].strip().replace(" ", "_").lower()
    ruta_pasos = os.path.join(DATA_DIR, f"pasos_{nombre_seguro}.csv")
    if not os.path.exists(ruta_pasos):
        return
        
    datos_metodos = {}
    with open(ruta_pasos, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for fila in reader:
            metodo = fila[0]
            n = int(fila[1])
            x_val = float(fila[2])
            if metodo not in datos_metodos:
                datos_metodos[metodo] = {"iters": [], "x_vals": []}
            datos_metodos[metodo]["iters"].append(n)
            datos_metodos[metodo]["x_vals"].append(x_val)
            
    raiz_real = func_info["raiz_exacta"]
    estilos = {
        "Bisección": ("#1f77b4", "o", "-"),
        "Falsa Posición": ("#ff7f0e", "s", "--"),
        "Punto Fijo": ("#2ca02c", "^", "-."),
        "Secante": ("#9467bd", "d", "-"),
        "Newton-Raphson": ("#d62728", "v", "-"),
        "Newton Mejorado": ("#8c564b", "*", ":")
    }
    
    plt.figure(figsize=(9, 5.5), dpi=150)
    for metodo, vals in datos_metodos.items():
        if len(vals["iters"]) > 0:
            errores = [max(abs(x - raiz_real), 1e-16) for x in vals["x_vals"]]
            color, marker, linestyle = estilos.get(metodo, ("black", "o", "-"))
            plt.semilogy(vals["iters"], errores, label=f"{metodo} ({len(vals['iters'])} iter)",
                         color=color, marker=marker, linestyle=linestyle, markersize=5, linewidth=1.8)
            
    plt.axhline(1e-6, color="black", linestyle=":", linewidth=1.2, label="Tolerancia (1e-6)")
    plt.title(f"Convergencia |Error| vs Iteración: {func_info['nombre_corto']}", fontsize=12, fontweight="bold")
    plt.xlabel("Iteración (n)", fontsize=11)
    plt.ylabel("|x_n - raíz| (Escala Log)", fontsize=11)
    plt.grid(True, which="both", linestyle=":", alpha=0.6)
    plt.legend(loc="best", fontsize=8.5)
    plt.tight_layout()
    
    ruta_guardado = os.path.join(ASSETS_DIR, f"convergencia_{nombre_seguro}.png")
    plt.savefig(ruta_guardado)
    plt.close()


def graficar_resumen_iteraciones(catalogo):
    #lee el CSV resumen y genera el gráfico comparativo global de barras.
    ruta_resumen = os.path.join(DATA_DIR, "resumen_convergencia.csv")
    if not os.path.exists(ruta_resumen):
        return
        
    iter_dict = {}
    with open(ruta_resumen, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for fila in reader:
            cat = fila[0]
            met = fila[2]
            conv = (fila[3] == "Si")
            it = int(fila[4]) if conv else 0
            if met not in iter_dict:
                iter_dict[met] = {}
            iter_dict[met][cat] = it
            
    nombres_funciones = [f["categoria"] for f in catalogo]
    etiquetas_eje = [cat.replace(" (", "\n(") for cat in nombres_funciones]
    nombres_metodos = ["Bisección", "Falsa Posicion", "Punto Fijo", "Secante", "Newton-Raphson", "Newton Mejorado"]
    colores = ["#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd", "#d62728", "#8c564b"]
    
    x = np.arange(len(nombres_funciones))
    width = 0.13
    
    plt.figure(figsize=(12, 6), dpi=150)
    for idx, metodo in enumerate(nombres_metodos):
        iteraciones = [iter_dict.get(metodo, {}).get(cat, 0) for cat in nombres_funciones]
        pos = x + (idx - 2.5) * width
        barras = plt.bar(pos, iteraciones, width, label=metodo, color=colores[idx])
        
        for barra, val in zip(barras, iteraciones):
            if val > 0:
                plt.text(barra.get_x() + barra.get_width()/2.0, val + 0.8,
                         f"{val}", ha="center", va="bottom", fontsize=7.5, fontweight="bold")
            else:
                plt.text(barra.get_x() + barra.get_width()/2.0, 1.5,
                         "X", ha="center", va="bottom", fontsize=8, color="red", fontweight="bold")
                
    plt.title("Resumen Comparativo: Iteraciones hasta Converger (Tolerancia 1e-6)", fontsize=13, fontweight="bold")
    plt.xlabel("Categoría de Función", fontsize=11)
    plt.ylabel("Número de Iteraciones (X = No aplica / No converge)", fontsize=11)
    plt.xticks(x, etiquetas_eje, fontsize=9.5)
    plt.ylim(0, 45)
    plt.grid(axis="y", linestyle=":", alpha=0.7)
    plt.legend(loc="upper right", fontsize=9)
    plt.tight_layout()
    
    ruta_guardado = os.path.join(ASSETS_DIR, "resumen_iteraciones.png")
    plt.savefig(ruta_guardado)
    plt.close()


def main():
    catalogo = obtener_catalogo_funciones()

    for func_info in catalogo:
        graficar_funcion_con_raiz(func_info)
        graficar_convergencia(func_info)
        
    graficar_resumen_iteraciones(catalogo)

if __name__ == "__main__":
    main()