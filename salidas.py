
from registrar import inventario


registros_salida = []

def sacar_producto():
    nombre = input("Nombre del producto a retirar: ").strip().title()
    if nombre in inventario:
        try:
            cantidad = int(input("Cantidad a retirar: "))
            if cantidad <= inventario[nombre]["cantidad"]:
                inventario[nombre]["cantidad"] -= cantidad
                
                # Calcular el valor total de la salida
                precio_unitario = inventario[nombre]["precio"]
                valor_total = precio_unitario * cantidad

                # Guardamos el registro de salida con valor
                registros_salida.append({
                    "producto": nombre,
                    "cantidad": cantidad,
                    "valor_total": valor_total
                })

                print(f" Se retiraron {cantidad} unidades de {nombre} cuyo valor fue de {valor_total:.2f}")
            else:
                print(" No hay suficiente cantidad en inventario.")
        except ValueError:
            print(" Error: cantidad inválida.")
    else:
        print(" Producto no encontrado en inventario.")

def ver_registros_salida():
    if not registros_salida:
        print(" No hay registros de salida.")
    else:
        print("\n--- Registros de salida ---")
        for registro in registros_salida:
            print(f"Producto: {registro['producto']} | Cantidad retirada: {registro['cantidad']} | Valor total: {registro['valor_total']:.2f}")
