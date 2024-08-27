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
        opciones = int(input("""
            1. comprar producto
            2. vender producto
            3. imprmir historial de compras
            =>
            """))
        #primera opcion
        while  opciones == 1:
            print("<----------Comprar---------->")
            nombreProducto = input("Ingrese el nombre del producto: ")
            precioProducto = float(input("Ingrese el precio del producto: "))
            cantidadProducto = int(input("Ingrese la cantidad del producto: "))
            porcentajeUtilidadProducto = float(input("Ingrese el porcentaje de utilidad del producto: "))
            for producto in productos:
                #Actualizamos la cantidad de producto si el producto ya existe
                if producto[0] == nombreProducto:
                    # Si el producto ya existe se le cambia el precio, la cantidad y el porcentaje de utilidad 
                    cantidadAnterior = producto[2]
                    cantidadAnterior += cantidadProducto
                    
                    porcentajeUtilidadProductoAnterior = producto[3]
                    porcentajeUtilidadProductoAnterior = porcentajeUtilidadProducto
                    
                    precioAnterior = producto[1]
                    #suma porcentaje de utilizad al precio del producto
                    precioAnterior = precioProducto * (porcentajeUtilidadProducto / 100)
                else:
                    #suma porcentaje de utilizad al precio del producto
                    porcentajeUtilidadProducto = porcentajeUtilidadProducto
                    precioProducto = precioProducto * (porcentajeUtilidadProducto / 100)
                    #agreamos el producto a la lista productos
                    productos.extend(nombreProducto,precioProducto,cantidadProducto,porcentajeUtilidadProducto) #cargo el producto
                break
            #agregar a compras el el producto digitado y el nombre del usuario
            compras.extend(userName,nombreProducto,cantidadProducto,precioProducto)
            historialDeCompras.extend(userName,compras)
            salir = input("si desea parar ingrese (x): ")
            if(salir == "x"):
                break
        #segunda opcion
        while opciones == 2:
            print("<----------Vender---------->")
            nombreProducto = input("Ingrese el nombre del producto: ")
            cantidadProducto = int(input("Ingrese la cantidad del producto: "))
            for producto in productos:
                if producto[0] == nombreProducto:
                    if producto[2] >= cantidadProducto:
                        saldo += cantidadProducto * producto[1]
                        producto[2] -= cantidadProducto
                        ventas.extend(userName, nombreProducto, producto[1], cantidadProducto)
                        historialDeCompras.extend(userName, [compra[0] for compra in compras if compra[1] == nombreProducto])
                        saldos.extend(userName, saldo)
                        break
                    else:
                        print("No hay suficiente stock para vender este producto")
                        break
            if(salir == "x"):
                break
        #tercera opcion
        while opciones == 3:
            for historial in historialDeCompras:
                if userName == historial:
                    historialDeUsuario = []
                    historialDeUsuario.extend(historial)
                    print(f"Su historial de compras es:{historialDeUsuario}")
                    break
                else: print("Usted no ha comprado ningun producto aun")
                break

    salir = input("Si desea salir ingrese (salir)").lower()
    if salir == "salir":
        break
        