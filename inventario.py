
from registrar import inventario

def ver_inventario():
    if not inventario:
        print("Inventario vacío.")
    else:
        print("\n--- Inventario Actual ---")
        for nombre, datos in inventario.items():
            print(f"{nombre}  Precio: {datos['precio']}, Cantidad: {datos['cantidad']}")
