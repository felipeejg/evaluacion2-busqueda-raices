import numpy as np

def biseccion(f, a, b, tol=1e-6, max_iter=100):
    #Método de Bisección (Cerrado - Orden Lineal).
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        return {
            "convergio": False, "raiz": np.nan, "iteraciones": 0,
            "error": np.nan, "pasos": [], "motivo": "Sin cambio de signo f(a)*f(b) < 0"
        }
    
    pasos = []
    p_ant = a
    for n in range(1, max_iter + 1):
        p = (a + b) / 2.0
        fp = f(p)
        error = abs(p - p_ant) if n > 1 else abs(b - a) / 2.0
        pasos.append((n, p, abs(fp), error))
        
        if abs(fp) < tol or error < tol:
            return {
                "convergio": True, "raiz": p, "iteraciones": n,
                "error": error, "pasos": pasos, "motivo": "Convergencia exitosa"
            }
        
        if fa * fp < 0:
            b = p
            fb = fp
        else:
            a = p
            fa = fp
        p_ant = p
        
    return {
        "convergio": False, "raiz": p, "iteraciones": max_iter,
        "error": error, "pasos": pasos, "motivo": "Maximo de iteraciones alcanzado"
    }


def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):
    #Método de Falsa Posición (Cerrado - Orden Lineal).
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        return {
            "convergio": False, "raiz": np.nan, "iteraciones": 0,
            "error": np.nan, "pasos": [], "motivo": "Sin cambio de signo f(a)*f(b) < 0"
        }
    
    pasos = []
    p_ant = a
    for n in range(1, max_iter + 1):
        if abs(fb - fa) < 1e-15:
            return {
                "convergio": False, "raiz": p_ant, "iteraciones": n,
                "error": np.nan, "pasos": pasos, "motivo": "Division por cero"
            }
            
        p = b - fb * (b - a) / (fb - fa)
        fp = f(p)
        error = abs(p - p_ant) if n > 1 else abs(b - a)
        pasos.append((n, p, abs(fp), error))
        
        if abs(fp) < tol or error < tol:
            return {
                "convergio": True, "raiz": p, "iteraciones": n,
                "error": error, "pasos": pasos, "motivo": "Convergencia exitosa"
            }
            
        if fa * fp < 0:
            b = p
            fb = fp
        else:
            a = p
            fa = fp
        p_ant = p
        
    return {
        "convergio": False, "raiz": p, "iteraciones": max_iter,
        "error": error, "pasos": pasos, "motivo": "Maximo de iteraciones alcanzado"
    }

def punto_fijo(f, g, x0, tol=1e-6, max_iter=100):
    #método de Iteración de Punto Fijo x = g(x) (Abierto - Orden Lineal).
    pasos = []
    x = float(x0)
    for n in range(1, max_iter + 1):
        try:
            x_next = float(g(x))
        except (ValueError, ZeroDivisionError, OverflowError):
            return {
                "convergio": False, "raiz": x, "iteraciones": n,
                "error": np.nan, "pasos": pasos, "motivo": "Indefinicion en g(x)"
            }
            
        error = abs(x_next - x)
        fx_val = abs(f(x_next)) if not np.isnan(x_next) else np.nan
        pasos.append((n, x_next, fx_val, error))
        
        if error < tol or fx_val < tol:
            return {
                "convergio": True, "raiz": x_next, "iteraciones": n,
                "error": error, "pasos": pasos, "motivo": "Convergencia exitosa"
            }
        if error > 1e10 or np.isnan(x_next):
            return {
                "convergio": False, "raiz": x_next, "iteraciones": n,
                "error": error, "pasos": pasos, "motivo": "Divergencia detectada"
            }
            
        x = x_next
        
    return {
        "convergio": False, "raiz": x, "iteraciones": max_iter,
        "error": error, "pasos": pasos, "motivo": "Maximo de iteraciones alcanzado"
    }


def secante(f, x0, x1, tol=1e-6, max_iter=100):
    # método de la Secante (Abierto - Orden Superlineal ~1.618).
    pasos = []
    p0, p1 = float(x0), float(x1)
    for n in range(1, max_iter + 1):
        fp0, fp1 = f(p0), f(p1)
        if abs(fp1 - fp0) < 1e-15:
            return {
                "convergio": False, "raiz": p1, "iteraciones": n,
                "error": np.nan, "pasos": pasos, "motivo": "Diferencia f(p1)-f(p0) nula"
            }
            
        p = p1 - fp1 * (p1 - p0) / (fp1 - fp0)
        error = abs(p - p1)
        fp = f(p)
        pasos.append((n, p, abs(fp), error))
        
        if abs(fp) < tol or error < tol:
            return {
                "convergio": True, "raiz": p, "iteraciones": n,
                "error": error, "pasos": pasos, "motivo": "Convergencia exitosa"
            }
            
        p0, p1 = p1, p
        
    return {
        "convergio": False, "raiz": p1, "iteraciones": max_iter,
        "error": error, "pasos": pasos, "motivo": "Maximo de iteraciones alcanzado"
    }

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    # metodo de Newton-Raphson (Abierto - Orden Cuadrático en raíces simples).
    pasos = []
    p0 = float(x0)
    for n in range(1, max_iter + 1):
        fp0 = f(p0)
        dfp0 = df(p0)
        if abs(dfp0) < 1e-15:
            return {
                "convergio": False, "raiz": p0, "iteraciones": n,
                "error": np.nan, "pasos": pasos, "motivo": "Derivada nula (tangente horizontal)"
            }
            
        p = p0 - fp0 / dfp0
        error = abs(p - p0)
        fp = f(p)
        pasos.append((n, p, abs(fp), error))
        
        if abs(fp) < tol or error < tol:
            return {
                "convergio": True, "raiz": p, "iteraciones": n,
                "error": error, "pasos": pasos, "motivo": "Convergencia exitosa"
            }
            
        p0 = p
        
    return {
        "convergio": False, "raiz": p0, "iteraciones": max_iter,
        "error": error, "pasos": pasos, "motivo": "Maximo de iteraciones alcanzado"
    }


def newton_modificado(f, df, d2f, x0, tol=1e-6, max_iter=100):
    # metodo de Newton-Raphson Mejorado (Abierto - Orden Cuadrático en raíces múltiples).
    pasos = []
    p0 = float(x0)
    for n in range(1, max_iter + 1):
        fp0 = f(p0)
        dfp0 = df(p0)
        d2fp0 = d2f(p0)
        
        denom = (dfp0 ** 2) - fp0 * d2fp0
        if abs(denom) < 1e-15:
            return {
                "convergio": False, "raiz": p0, "iteraciones": n,
                "error": np.nan, "pasos": pasos, "motivo": "Denominador D = 0"
            }
            
        p = p0 - (fp0 * dfp0) / denom
        error = abs(p - p0)
        fp = f(p)
        pasos.append((n, p, abs(fp), error))
        
        if abs(fp) < tol or error < tol:
            return {
                "convergio": True, "raiz": p, "iteraciones": n,
                "error": error, "pasos": pasos, "motivo": "Convergencia exitosa"
            }
            
        p0 = p
        
    return {
        "convergio": False, "raiz": p0, "iteraciones": max_iter,
        "error": error, "pasos": pasos, "motivo": "Maximo de iteraciones alcanzado"
    }