# 10. teniendo una lista con varias listas anidadas de productos,
# cada una con la siguiente informaci�n
# Nombre del producto, saldo anterior, precio de compra, porcentaje de utilidad
# calcular el precio de venta, solictar las compras y las ventas y generar nuevo saldo

usuarios = [] #["nombre"]
productos = [] # lista de todos los productos estructura ["nombre","precio","cantidad","porcentaje de utilidad"]
ventas = [] #["nombre de usuario", "nombre de producto", "precio de producto", "cantidad vendida(se resta a la cantidad del producto)"]
saldos = [] #["nombre de usuario", saldo]
compras = [] #["nombre de usuario", "nombre de producto", "cantidad (se agrega cantidad al producto)", "precio de producto"]
historialDeCompras = [] #["nombre de usuario"[compras]]
listaFinal = [] # [usuarios[productos][ventas][saldos][compras][historialDeCompras]]

while True:
    userName = input("Ingrese su nombre: ")
    saldo = float(input("Ingrese su saldo: "))
    start = False
    if userName == "" or saldo =="":
        start = False
    else: start = True

    while start:
        opt1 = int(input("1. Comprar producto"))
        opt2 = int(input("2. Vender producto"))
        opt3 = int(input("3. Imprimir historial de compras"))
        #primera opcion
        while opt1:
            print("<----------Comprar---------->")
            nombreProducto = input("Ingrese el nombre del producto: ")
            precioProducto = float(input("Ingrese el precio del producto: "))
            cantidadProducto = int(input("Ingrese la cantidad del producto: "))
            porcentajeUtilidadProducto = float(input("Ingrese el porcentaje de utilidad del producto: "))
            productos.append(nombreProducto,precioProducto,cantidadProducto,porcentajeUtilidadProducto) #cargo el producto
            for producto in productos:
                if producto == nombreProducto:
                    pass
            historialDeCompras.append(userName,compras)
            salir = input("si desea parar ingrese (x): ")
            if(salir == "x"):
                break
        #segunda opcion
        while opt2:
            print("<----------Vender---------->")
            nombreProducto = input("Ingrese el nombre del producto: ")
            cantidadProducto = int(input("Ingrese la cantidad del producto: "))
            for producto in productos:
                if producto[0] == nombreProducto:
                    if producto[2] >= cantidadProducto:
                        saldo += cantidadProducto * producto[1]
                        producto[2] -= cantidadProducto
                        ventas.append(userName, nombreProducto, producto[1], cantidadProducto)
                        historialDeCompras.append(userName, [compra[0] for compra in compras if compra[1] == nombreProducto])
                        saldos.append(userName, saldo)
                        break
                    else:
                        print("No hay suficiente stock para vender este producto")
                        break
            if(salir == "x"):
                break
        #tercera opcion
        while opt3:
            
            if(salir == "x"):
                break

    salir = input("Si desea salir ingrese (salir)").lower()
    if salir == "salir":
        break
        