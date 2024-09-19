def mostrar_menu():
    print("1. Saldo anterior")
    print("2. Compras y ventas")
    print("3. Otras compras y ventas")
    print("4. Mostrar saldo y finalizar producto")
    print("5. Salir")

def solicitar_compras():
    acompras = 0.0
    while True:
        compras = float(input("Ingrese la cantidad comprada. 0 para terminar: "))
        if compras == 0:
            break
        acompras += compras
    return acompras

def solicitar_ventas():
    aventas = 0.0
    while True:
        ventas = float(input("Ingrese las ventas. 0 para terminar: "))
        if ventas == 0:
            break
        aventas += ventas
    return aventas

def solicitar_otras_compras():
    aocompras = 0.0
    while True:
        ocompras = float(input("Ingrese las otras compras. 0 para terminar: "))
        if ocompras == 0:
            break
        aocompras += ocompras
    return aocompras

def solicitar_otras_ventas():
    aoventas = 0.0
    while True:
        oventas = float(input("Ingrese las otras ventas. 0 para terminar: "))
        if oventas == 0:
            break
        aoventas += oventas
    return aoventas

def procesar_producto():
    nombre = input("Ingrese nombre del producto: ")
    saldo_anterior = float(input("¿Cuántos artículos tenía?: "))
    acompras = 0.0
    aventas = 0.0
    aocompras = 0.0
    aoventas = 0.0

    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            acompras += solicitar_compras()
        elif opcion == 2:
            aventas += solicitar_ventas()
        elif opcion == 3:
            aocompras += solicitar_otras_compras()
            aoventas += solicitar_otras_ventas()
        elif opcion == 4:
            nuevo_saldo = saldo_anterior + acompras - aventas + aocompras - aoventas
            print(f"Producto: {nombre}")
            print(f"Saldo anterior: {saldo_anterior}")
            print(f"Compras: {acompras}, Ventas: {aventas}")
            print(f"Otras compras: {aocompras}, Otras ventas: {aoventas}")
            print(f"Nuevo saldo: {nuevo_saldo}")
            break
        elif opcion == 5:
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def gestionar_productos():
    n = int(input("¿Cuántos productos desea procesar?: "))
    for i in range(n):
        procesar_producto()

# Ejecutar el programa
gestionar_productos()   
