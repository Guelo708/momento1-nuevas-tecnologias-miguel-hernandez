from menu import mostrar_menu
from registrar import registrar_producto, inventario


continuar = True

while continuar:

    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_producto()
        
    elif opcion == "7": 
        print("Saliendo del sistema...")
        continuar = False
    else:
        print("Opción seleccionada:", opcion)

