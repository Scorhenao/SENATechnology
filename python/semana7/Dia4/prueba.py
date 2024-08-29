# 1. recorrer una matriz de productos y mostrar cada producto completo
# 2. mostrar cada atributo de cada producto desmembrado
# 3. calcular precio de venta, solicitar saldo anterior que es el total de los productos ya asignados y mostrar menu para comprar o vender 
# 4. calcular el nuevo saldo, lo que tenia + que compro - que vendio
# 5. adicionar lo de 3 y 4
# 6. cuanta plata tengo en el negocio? precios de compra * nuevo saldo. Plata invertida en el negocio
# 7. cuanta plata recive si vende el negocio comleto ganando un 30% precio de venta*nuevo saldo + 30%
precioDeVenta = 0
precioDeVentaTotal = 0
productos = [
    ["x",10000,0.4],
    ["y",20000,0.3],
    ["z",30000,0.5]
    ]
#Mostrar cada producto
for i in productos:
    #Quitar [] para que se vea mejor
    print(f"\n Producto: {i}")
    print(f"Nombre de producto: {i[0]}")
    print(f"Precio de producto: {i[1]} ")
    print(f"Porcentaje de utilidad: {i[2]}")

    #Calcular precio de venta
    precio = i[1]
    porcentajeDeUtilidad = i[2]
    precioDeVenta = precio * porcentajeDeUtilidad + precio
    print(f"Precio de venta por producto: {precioDeVenta}")
    
    print("\n------Comprar------")
    canidadAnterior = int(input(f"Ingrese la cantidad anterior del producto {i[0]}: "))
    cantidadComprada = int(input(f"Seleccione la cantidad que compro de {i[0]}:"))
    cantidadtTotal = cantidadComprada + canidadAnterior
    precioDeVentaTotal += i[1] * cantidadtTotal

    print("\n------Vender------")
    print(f"Seleccione la cantidad vendida de: {i[0]}")
    cantidadComprada = int(input("Ingrese la cantidad: "))
    precioDeVentaTotal -= i[1] * cantidadtTotal

    print(f"\nEl saldo anterior del producto {i[0]} es {canidadAnterior}")
    print(f"El saldo comprado es: {cantidadComprada} ")
    print(f"El nuevo saldo es del producto {i[0]} es {cantidadtTotal}")
# cuanto vale el negocio en total
print(f"\n El valor del mercado es: {precioDeVentaTotal * 0.3}")