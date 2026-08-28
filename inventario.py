# inventario.py

from registrar import inventario

def ver_inventario():
    if not inventario:
        print("Inventario vacío.")
    else:
        print("\n--- Inventario Actual ---")
        total_inventario = 0
        for nombre, datos in inventario.items():
            precio_unitario = datos["precio"]
            cantidad = datos["cantidad"]
            valor_total = precio_unitario * cantidad
            total_inventario += valor_total
            print(f"{nombre} -> Precio: {precio_unitario}, Cantidad: {cantidad}, Valor total: {valor_total}")
        
        print(f"\n Valor total del inventario: {total_inventario}")

