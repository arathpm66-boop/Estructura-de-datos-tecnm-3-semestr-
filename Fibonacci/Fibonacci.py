import time

# 1. Solución Recursiva (Elegante pero lenta para n grandes)
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# 2. Solución Iterativa (Mucho más rápida y eficiente en memoria)
def fibonacci_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# --- Pruebas y Tiempos ---
n = 30  # Prueba con 30 para notar la diferencia de tiempo

print(f"--- Comparación para n = {n} ---")

# Medir tiempo Recursivo
inicio = time.time()
res_rec = fibonacci_recursivo(n)
fin = time.time()
tiempo_rec = fin - inicio
print(f"Recursivo: Resultado = {res_rec}, Tiempo = {tiempo_rec:.6f} seg")

# Medir tiempo Iterativo
inicio = time.time()
res_ite = fibonacci_iterativo(n)
fin = time.time()
tiempo_ite = fin - inicio
print(f"Iterativo: Resultado = {res_ite}, Tiempo = {tiempo_ite:.6f} seg")