class Pila:
    def __init__(self, capacidad_maxima=8):
        self.items = []
        self.capacidad = capacidad_maxima
        self.tope = 0  # Inicialmente vacía

    def insertar(self, valor):
        print(f"Intentando insertar: {valor}")
        if self.tope < self.capacidad:
            self.items.append(valor)
            self.tope += 1
            self.mostrar_estado()
        else:
            print("ERROR: Desbordamiento (Overflow). La pila está llena.")

    def eliminar(self, variable_destino):
        print(f"Intentando eliminar (guardar en {variable_destino})")
        if self.tope > 0:
            eliminado = self.items.pop()
            self.tope -= 1
            print(f"-> Se eliminó: {eliminado}")
            self.mostrar_estado()
            return eliminado
        else:
            print("!!! ERROR: Subdesbordamiento (Underflow). No hay elementos para eliminar.")
            return None

    def mostrar_estado(self):
        print(f"Pila actual: {self.items} | TOPE = {self.tope}")
        print("-" * 30)

# --- EJECUCIÓN DEL PROBLEMA ---
mi_pila = Pila(8)

# a, b. Insertar X, Y
mi_pila.insertar("X")
mi_pila.insertar("Y")

# c, d, e. Eliminar Z, T, U
mi_pila.eliminar("Z")
mi_pila.eliminar("T")
mi_pila.eliminar("U") # Aquí debería saltar el error de Underflow

# f, g. Insertar V, W
mi_pila.insertar("V")
mi_pila.insertar("W")

# h. Eliminar p
mi_pila.eliminar("p")

# i. Insertar R
mi_pila.insertar("R")

print("\n--- RESULTADO FINAL ---")
print(f"Elementos restantes: {len(mi_pila.items)}")
print(f"Puntero TOPE final: {mi_pila.tope}")