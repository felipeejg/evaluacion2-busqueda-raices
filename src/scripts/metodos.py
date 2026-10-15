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