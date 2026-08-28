


inventario = {}

def registrar_producto():
    
    nombre = input("Nombre del producto: ").strip().title()
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}
        print(" Producto registrado exitosamente.")
    except ValueError:
        print(" Error: precio o cantidad inválidos.")
