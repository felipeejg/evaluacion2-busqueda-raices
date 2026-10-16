#Ejecuta secuencialmente la generación de datos numéricos (CSVs) y la renderización gráfica (PNGs).
import generar_datos
import graficar

def main():
    generar_datos.main()
    graficar.main()

if __name__ == "__main__":
    main()