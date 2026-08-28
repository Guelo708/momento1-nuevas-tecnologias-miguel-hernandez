# main.py

# main.py

# main.py

from menu import mostrar_menu
from registrar import registrar_producto, inventario
from inventario import ver_inventario
from salidas import sacar_producto, ver_registros_salida

continuar = True
while continuar:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        ver_inventario()
    elif opcion == "3":
        sacar_producto()
    elif opcion == "4":
        ver_registros_salida()
    elif opcion == "7":  # opción de salir
        print("Saliendo del sistema...")
        continuar = False
    else:
        print("Opción seleccionada:", opcion)




