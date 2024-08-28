# 10. teniendo una lista con varias listas anidadas de productos,
# cada una con la siguiente informaci�n
# Nombre del producto, saldo anterior, precio de compra, porcentaje de utilidad
# calcular el precio de venta, solictar las compras y las ventas y generar nuevo saldo

usuarios = []  # ["nombre"]
productos = []  # lista de todos los productos estructura ["nombre","precio","cantidad","porcentaje de utilidad"]
ventas = []  # ["nombre de usuario", "nombre de producto", "precio de producto", "cantidad vendida (se resta a la cantidad del producto)"]
compras = []  # ["nombre de usuario", "nombre de producto", "cantidad (se agrega cantidad al producto)", "precio de producto"]
historialDeCompras = []  # ["nombre de usuario", [compras]]
historialDeVentas = []  # ["nombre de usuario", [ventas]]
listaFinal = []  # [usuarios, productos, ventas, saldos, compras, historialDeCompras, historialDeVentas]

while True:
    print("Bienvenido")
    userName = input("Ingrese su nombre: ")
    start = False
    if userName == "":
        start = False
    else:
        start = True

    while start:
        opciones = input("""
            1. comprar producto
            2. vender producto
            3. imprimir historial de compras
            4. imprimir historial de ventas
            x. salir
            =>""").lower()

        # Primera opción: Comprar producto
        if opciones == '1':
            while True:
                print("<----------Comprar---------->")
                nombreProducto = input("Ingrese el nombre del producto: ")
                precioProducto = float(input("Ingrese el precio del producto: "))
                cantidadProducto = int(input("Ingrese la cantidad del producto: "))
                porcentajeUtilidadProducto = float(input("Ingrese el porcentaje de utilidad del producto: "))

                productoExistente = False
                for producto in productos:
                    if producto[0] == nombreProducto:
                        # Si el producto ya existe, actualizamos la cantidad y el precio
                        producto[2] += cantidadProducto
                        producto[3] = porcentajeUtilidadProducto
                        producto[1] = precioProducto * (1 + porcentajeUtilidadProducto / 100)
                        productoExistente = True
                        break

                if not productoExistente:
                    # Si el producto no existe, lo agregamos a la lista productos
                    productos.append([nombreProducto, precioProducto * (1 + porcentajeUtilidadProducto / 100), cantidadProducto, porcentajeUtilidadProducto])
                
                # Agregar a compras el producto digitado y el nombre del usuario
                compras.append([userName, nombreProducto, cantidadProducto, precioProducto])
                
                # Actualizar el historial de compras
                usuarioHistorial = next((item for item in historialDeCompras if item[0] == userName), None)
                if usuarioHistorial:
                    # Si ya existe el historial de compras para el usuario, se añade la nueva compra
                    usuarioHistorial[1].append([userName, nombreProducto, cantidadProducto, precioProducto])
                else:
                    # Si no existe el historial, se crea uno nuevo para el usuario
                    historialDeCompras.append([userName, [[userName, nombreProducto, cantidadProducto, precioProducto]]])
                
                salir = input("Si desea parar la compra ingrese (x) o presione Enter para continuar: ")
                if salir.lower() == "x":
                    break

        # Segunda opción: Vender producto
        elif opciones == '2':
            while True:
                print("<----------Vender---------->")
                nombreProducto = input("Ingrese el nombre del producto: ")
                cantidadProducto = int(input("Ingrese la cantidad del producto: "))

                productoEncontrado = False
                for producto in productos:
                    if producto[0] == nombreProducto:
                        if producto[2] >= cantidadProducto:
                            # Se calcula el precio total de la venta
                            totalVenta = cantidadProducto * producto[1]
                            # Se actualiza la cantidad del producto
                            producto[2] -= cantidadProducto
                            # Se registra la venta
                            ventas.append([userName, nombreProducto, producto[1], cantidadProducto, totalVenta])
                            productoEncontrado = True
                            break
                        else:
                            print("No hay suficiente stock para vender este producto")
                            productoEncontrado = True
                            break
                
                if not productoEncontrado:
                    print("El producto no existe.")
                
                # Actualizar el historial de ventas
                usuarioHistorialVentas = next((item for item in historialDeVentas if item[0] == userName), None)
                if usuarioHistorialVentas:
                    # Si ya existe el historial de ventas para el usuario, se añade la nueva venta
                    usuarioHistorialVentas[1].append([userName, nombreProducto, producto[1], cantidadProducto, totalVenta])
                else:
                    # Si no existe el historial, se crea uno nuevo para el usuario
                    historialDeVentas.append([userName, [[userName, nombreProducto, producto[1], cantidadProducto, totalVenta]]])

                salir = input("Si desea parar la venta ingrese (x) o presione Enter para continuar: ")
                if salir.lower() == "x":
                    break

        # Tercera opción: Imprimir historial de compras
        elif opciones == '3':
            historialDeUsuario = next((item for item in historialDeCompras if item[0] == userName), None)
            if historialDeUsuario:
                print(f"Su historial de compras es: {historialDeUsuario[1]}")
            else:
                print("Usted no ha comprado ningún producto aún")

        # Cuarta opción: Imprimir historial de ventas
        elif opciones == '4':
            historialDeUsuarioVentas = next((item for item in historialDeVentas if item[0] == userName), None)
            if historialDeUsuarioVentas:
                print(f"Su historial de ventas es: ")
                for venta in historialDeUsuarioVentas[1]:
                    print(f"Usuario: {venta[0]}, Producto: {venta[1]}, Precio por unidad: {venta[2]}, Cantidad vendida: {venta[3]}, Total: {venta[4]}")
            else:
                print("Usted no ha vendido ningún producto aún")

        # Salir del menú de opciones
        elif opciones == 'x':
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

    # Agregar usuario a la lista final
    if userName not in usuarios:
        usuarios.append(userName)

    # Imprimir la lista final ordenada
    listaFinal = [usuarios, productos, ventas, compras, historialDeCompras, historialDeVentas]
    print("\nLista Final:")
    print(f"Usuarios: {usuarios}")
    print(f"Productos: {productos}")
    print(f"Ventas: {ventas}")
    print(f"Compras: {compras}")
    print(f"Historial de Compras: {historialDeCompras}")
    print(f"Historial de Ventas: {historialDeVentas}")

    salir = input("Si desea salir ingrese (salir)").lower()
    if salir == "salir":
        break
