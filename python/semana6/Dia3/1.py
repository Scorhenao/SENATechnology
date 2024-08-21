# crear listas con nombres,precios,cantidades y totales de los productos 
# crer un menu donde pueda ingresar,vender,imprimir,borrar,mostrar mayores y menores. (productos)

nombres = []
precios = []
cantidades = []
totales = []

def menu():
    print("1. Ingresar producto")
    print("2. Vender producto")
    print("3. Imprimir productos")
    print("4. Borrar producto")
    print("5. Mostrar productos mayores")
    print("6. Mostrar productos menores")
    print("7. Salir")

def validar_opcion(opcion):
    match opcion:
        case 1:
            ingresar_producto()
        case 2:
            vender_producto()
        case 3:
            imprimir_productos()
        case 4:
            borrar_producto()
        case 5:
            mostrar_mayores()
        case 6:
            mostrar_menores()
        case 7:
            exit()

def ingresar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    nombres.append(nombre)
    precios.append(precio)
    cantidades.append(cantidad)
    print("Producto ingresado correctamente!")

def vender_producto():
    nombre = input("Ingrese el nombre del producto que desea vender: ")
    for index, producto in nombres:
        if nombre == producto:
            posicion = index 
            precio = precios[posicion]
            cantidad = cantidades[posicion]
            total = producto*precio / cantidad
            totales.append(total)
        else:
            print("producto no encontrado!")
def imprimir_productos():
    # juntar el nombre del producto, con su cantidad, su precio en un solo array
    productos = list(zip(nombres, cantidades, precios, totales))
    # ordenar los productos por el total en orden descendiente
    productos.sort(key=lambda x: x[3], reverse=True)
    for producto in productos:
        print(f"Producto: {producto[0]}, Cantidad: {producto[1]}, Precio: {producto[2]}, Total: {producto[3]}") 
    
def borrar_producto():
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")
    for index, producto in nombres:
        if nombre == producto:
            del nombres[index]
            del precios[index]
            del cantidades[index]
            del totales[index]
            print("Producto eliminado correctamente!")
        else:
            print("Producto no encontrado!")
def mostrar_mayores():
    #mostrar en la lista de totales el total mas alto
    print(f"El producto más caro es: {nombres[totales.index(max(totales))]} con un total de: {max(totales)}")
def mostrar_menores():
    #mostrar en la lista de totales el total mas bajo 
    print(f"El producto más barato es: {nombres[totales.index(min(totales))]} con un total de: {min(totales)}")

start = input("si desea empezar el programa digite (si)\n =>")
while start == "si" or start == "SI" or start == "Si" or start == "sI":
    menu()
    opciones = int(input("ingrese una opcion: "))
    validar_opcion(opciones)