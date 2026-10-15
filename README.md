# Evaluación 2: La raíz que se esconde
Asignatura: Computación Numérica - Laboratorio  
Unidad: Iteración funcional para ecuaciones - búsqueda de raíces y análisis de convergencia.

## Descripción del Proyecto
Este repositorio implementa y compara seis métodos numéricos de búsqueda de raíces (Bisección, Falsa Posición, Punto Fijo, Secante, Newton-Raphson y Newton-Raphson Mejorado) evaluados bajo un ambiente controlado (`tol = 1e-6`, `max_iter = 100`) sobre 6 funciones de distinta naturaleza (polinómica simple, polinómica con raíz doble, logarítmica, exponencial, trigonométrica y mixta).

## Estructura del Repositorio
* `README.md`: Instrucciones de configuración y ejecución.
* `requirements.txt`: Dependencias del proyecto (`numpy`, `matplotlib`, `pytest`).
* `informe.md`: Respuestas fundamentadas a las preguntas de convergencia y conclusiones.
* `src/scripts/metodos.py`: Implementación vectorizada/numérica de los 6 métodos de búsqueda de raíces.
* `src/scripts/funciones.py`: Catálogo de las 6 funciones con sus derivadas, funciones de iteración $g(x)$ y parámetros de ambiente controlado.
* `src/scripts/ejecutar_todo.py`: Script principal que valida el ambiente controlado (Bolzano/tangencia), ejecuta las corridas, exporta los archivos CSV en `src/data/` y genera las gráficas en `src/assets/`.
