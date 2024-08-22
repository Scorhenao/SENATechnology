# crear listas con nombres,precios,cantidades y totales de los productos 
# crer un menu donde pueda ingresar,vender,imprimir,borrar,mostrar mayores y menores. (productos)

nombres = []
precios = []
cantidades = []
totales = []

def menu():
    print("\n1. Ingresar producto")
    print("2. Vender producto")
    print("3. Imprimir productos")
    print("4. Borrar producto")
    print("5. Mostrar productos mayores")
    print("6. Mostrar productos menores")
    print("7. Salir")

def validar_opcion(opcion):
    if opcion == 1:
        ingresar_producto()
    elif opcion == 2:
        vender_producto()
    elif opcion == 3:
        imprimir_productos()
    elif opcion == 4:
        borrar_producto()
    elif opcion == 5:
        mostrar_mayores()
    elif opcion == 6:
        mostrar_menores()
    elif opcion == 7:
        exit()
    else:
        print("Opción no válida, por favor elige otra opción.")

def ingresar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    total = precio * cantidad
    nombres.append(nombre)
    precios.append(precio)
    cantidades.append(cantidad)
    totales.append(total)
    print("Producto ingresado correctamente!")

def vender_producto():
    nombre = input("Ingrese el nombre del producto que desea vender: ")
    if nombre in nombres:
        index = nombres.index(nombre)
        cantidad_vender = int(input(f"Ingrese la cantidad a vender (Disponible: {cantidades[index]}): "))
        if cantidad_vender <= cantidades[index]:
            cantidades[index] -= cantidad_vender
            totales[index] = precios[index] * cantidades[index]
            print(f"Has vendido {cantidad_vender} de {nombre}.")
        else:
            print("Cantidad insuficiente para vender.")
    else:
        print("Producto no encontrado!")

def imprimir_productos():
    productos = list(zip(nombres, cantidades, precios, totales))
    productos.sort(key=lambda x: x[3], reverse=True)
    for producto in productos:
        print(f"Producto: {producto[0]}, Cantidad: {producto[1]}, Precio: {producto[2]}, Total: {producto[3]}")

def borrar_producto():
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")
    if nombre in nombres:
        index = nombres.index(nombre)
        del nombres[index]
        del precios[index]
        del cantidades[index]
        del totales[index]
        print("Producto eliminado correctamente!")
    else:
        print("Producto no encontrado!")

def mostrar_mayores():
    if totales:
        max_total = max(totales)
        index = totales.index(max_total)
        print(f"El producto más caro es: {nombres[index]} con un total de: {max_total}")
    else:
        print("No hay productos en la lista.")

def mostrar_menores():
    if totales:
        min_total = min(totales)
        index = totales.index(min_total)
        print(f"El producto más barato es: {nombres[index]} con un total de: {min_total}")
    else:
        print("No hay productos en la lista.")

start = input("Si desea empezar el programa digite (si)\n => ").lower()
while start == "si":
    menu()
    opcion = int(input("Ingrese una opción: "))
    validar_opcion(opcion)
