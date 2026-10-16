# Evaluación 2: La raíz que se esconde
Asignatura: Computación Numérica - Laboratorio  
Unidad: Iteración funcional para ecuaciones - búsqueda de raíces y análisis de convergencia.

## Descripción del Proyecto
Este repositorio implementa y compara seis métodos numéricos de búsqueda de raíces (Bisección, Falsa Posición, Punto Fijo, Secante, Newton-Raphson y Newton-Raphson Mejorado) evaluados bajo un ambiente controlado (`tol = 1e-6`, `max_iter = 100`) sobre 6 funciones de distinta naturaleza (polinómica simple, polinómica con raíz doble, logarítmica, exponencial, trigonométrica y mixta).

## Estructura del Repositorio
evaluacion2-busqueda-raices/
├── README.md              # Documentación del entorno y ejecución de scripts
├── requirements.txt       # Dependencias del proyecto (numpy, matplotlib, pytest)
├── informe.md             # Informe técnico con respuestas de convergencia y conclusiones
├── .gitignore             # Filtro para ignorar entorno virtual y temporales de Python
└── src/
    ├── data/              # Archivos CSV generados por función y resumen consolidado
    ├── assets/            # Gráficos PNG generados (curvas de funciones, convergencia y resumen)
    └── scripts/
        ├── metodos.py         # Implementación matemática pura de los 6 métodos numéricos
        ├── funciones.py       # Catálogo de funciones, derivadas, función g(x) y parámetros
        ├── generar_datos.py   # Módulo numérico: ejecuta los métodos y genera los archivos CSV
        ├── graficar.py        # Módulo gráfico: lee los CSV y crea los gráficos PNG
        └── ejecutar_todo.py   # Ejecuta generar_datos.py y graficar.py
