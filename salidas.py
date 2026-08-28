

from registrar import inventario


registros_salida = []

def sacar_producto():
    nombre = input("Nombre del producto a retirar: ").strip().title()
    if nombre in inventario:
        try:
            cantidad = int(input("Cantidad a retirar: "))
            if cantidad <= inventario[nombre]["cantidad"]:
                inventario[nombre]["cantidad"] -= cantidad
                # Guardamos el registro de salida
                registros_salida.append({"producto": nombre, "cantidad": cantidad})
                print(f" Se retiraron {cantidad} unidades de {nombre}.")
            else:
                print(" No hay suficiente cantidad en inventario.")
        except ValueError:
            print(" Error: cantidad inválida.")
    else:
        print(" Producto no encontrado en inventario.")
