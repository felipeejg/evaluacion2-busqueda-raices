import numpy as np

def obtener_catalogo_funciones():
    """
    Catálogo de las 6 funciones evaluadas en ambiente controlado:
    Incluye f(x), primera derivada df(x), segunda derivada d2f(x),
    función de punto fijo g(x), intervalo [a, b] y estimaciones iniciales.
    """
    return [
        {
            "id": "polinomica_simple",
            "categoria": "Polinómica (raíz simple)",
            "nombre_corto": "f(x) = x³ - x - 2",
            "expresion_latex": r"$f(x) = x^3 - x - 2$",
            "f": lambda x: x**3 - x - 2,
            "df": lambda x: 3 * (x**2) - 1,
            "d2f": lambda x: 6 * x,
            "g": lambda x: np.cbrt(x + 2),
            "intervalo": (1.0, 2.0),
            "x0": 1.0,
            "x1": 2.0,
            "raiz_exacta": 1.5213797068045676,
            "tipo_raiz": "simple"
        },
        {
            "id": "polinomica_doble",
            "categoria": "Polinómica (raíz doble)",
            "nombre_corto": "f(x) = (x - 2)²",
            "expresion_latex": r"$f(x) = (x - 2)^2$",
            "f": lambda x: (x - 2.0)**2,
            "df": lambda x: 2.0 * (x - 2.0),
            "d2f": lambda x: 2.0 * np.ones_like(x) if isinstance(x, np.ndarray) else 2.0,
            "g": lambda x: x - 0.2 * ((x - 2.0)**2),
            "intervalo": (1.0, 3.0),
            "x0": 1.2,
            "x1": 1.5,
            "raiz_exacta": 2.0000000000000000,
            "tipo_raiz": "doble"
        },
        {
            "id": "logaritmica",
            "categoria": "Logarítmica",
            "nombre_corto": "f(x) = ln(x) + x - 4",
            "expresion_latex": r"$f(x) = \ln(x) + x - 4$",
            "f": lambda x: np.log(x) + x - 4.0,
            "df": lambda x: (1.0 / x) + 1.0,
            "d2f": lambda x: -1.0 / (x**2),
            "g": lambda x: 4.0 - np.log(x),
            "intervalo": (2.0, 3.0),
            "x0": 2.0,
            "x1": 3.0,
            "raiz_exacta": 2.9262710628557482,
            "tipo_raiz": "simple"
        },
        {
            "id": "exponencial",
            "categoria": "Exponencial",
            "nombre_corto": "f(x) = e⁻ˣ - x",
            "expresion_latex": r"$f(x) = e^{-x} - x$",
            "f": lambda x: np.exp(-x) - x,
            "df": lambda x: -np.exp(-x) - 1.0,
            "d2f": lambda x: np.exp(-x),
            "g": lambda x: np.exp(-x),
            "intervalo": (0.0, 1.0),
            "x0": 0.0,
            "x1": 1.0,
            "raiz_exacta": 0.5671432904097838,
            "tipo_raiz": "simple"
        },
        {
            "id": "trigonometrica",
            "categoria": "Trigonométrica",
            "nombre_corto": "f(x) = cos(x) - x",
            "expresion_latex": r"$f(x) = \cos(x) - x$",
            "f": lambda x: np.cos(x) - x,
            "df": lambda x: -np.sin(x) - 1.0,
            "d2f": lambda x: -np.cos(x),
            "g": lambda x: np.cos(x),
            "intervalo": (0.0, 1.0),
            "x0": 0.5,
            "x1": 1.0,
            "raiz_exacta": 0.7390851332151607,
            "tipo_raiz": "simple"
        },
        {
            "id": "mixta",
            "categoria": "Mixta",
            "nombre_corto": "f(x) = √x - cos(x)",
            "expresion_latex": r"$f(x) = \sqrt{x} - \cos(x)$",
            "f": lambda x: np.sqrt(x) - np.cos(x),
            "df": lambda x: (1.0 / (2.0 * np.sqrt(x))) + np.sin(x),
            "d2f": lambda x: (-1.0 / (4.0 * (x**1.5))) + np.cos(x),
            "g": lambda x: np.cos(x)**2,
            "intervalo": (0.1, 1.0),
            "x0": 0.5,
            "x1": 1.0,
            "raiz_exacta": 0.6417143708728826,
            "tipo_raiz": "simple"
        }
    ]