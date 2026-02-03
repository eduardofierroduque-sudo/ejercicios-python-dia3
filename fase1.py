# 1. Declara variables y tipos de datos
fruta = "Manzana"       # str
precio = 2.5            # float
cantidad = 8            # int

print(f"Fruta: {fruta}, Precio: {precio}, Cantidad: {cantidad}")

# 2. Usa un diccionario para almacenar datos
compra = {
    "fruta": fruta, 
    "precio": precio, 
    "cantidad": cantidad
}

# Muestra solo el nombre de la fruta y la cantidad
print(f"Compra registrada: {compra['fruta']} (x{compra['cantidad']})")

# 3. Calcula el total con operadores
total = compra["precio"] * compra["cantidad"]
print(f"Total bruto: {total}")

# 4. Aplica condicionales
# Regla: si cantidad > 5, aplicar 10% de descuento
if compra["cantidad"] > 5:
    descuento = total * 0.10
    total_final = total - descuento
    print(f"¡Se aplicó un 10% de descuento! Total a pagar: {total_final}")
else:
    total_final = total
    print(f"Total a pagar: {total_final}")