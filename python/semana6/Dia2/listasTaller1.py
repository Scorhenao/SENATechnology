# # Escribir un programa que almacene las asignaturas de un curso
# # (por ejemplo Matem�ticas, F�sica, Qu�mica, Historia y Lengua)
# # en una lista y la muestre por pantalla.

# materias = ["matematicas", "quimica","filosofia", "religion"]
# for elemento in materias:
#     print(elemento)

# # Escribir un programa que almacene las asignaturas de un curso
# # (por ejemplo Matem�ticas, F�sica, Qu�mica, Historia y Lengua) en una lista,
# # pregunte al usuario la nota que ha sacado en cada asignatura, y despu�s
# # las muestre por pantalla con el mensaje En <asignatura> has sacado <nota>
# # donde <asignatura> es cada una des las asignaturas de la lista y <nota>
# # cada una de las correspondientes notas introducidas por el usuario.


# materias = ["matematicas", "quimica","filosofia", "religion"]
# for elemento in materias:
#     nota = float(input("�Qu� nota has sacado en " + elemento + "?  "))
#     print("en ",elemento, "saque una nota de ", nota)


# #Escribir un programa que pregunte al usuario los n�meros ganadores de la loter�a primitiva,
# # los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# ganadores = []
# i = 0
# numeros = int(input("cuantos son los numeros ganadores ? "))
# for i in range(1, numeros+1):
#     ganador = int(input("Ingresa el " + str(i) + "  numero "))
#     ganadores.append(ganador)

# ganadores.sort()
# print(ganadores)




# #Escribir un programa que pregunte al usuario los n�meros ganadores de la loter�a primitiva,
# # los almacene en una lista y los muestre por pantalla ordenados de mayor a menor.

# ganadores = []
# i = 0
# numeros = int(input("cuantos son los numeros ganadores ? "))
# for i in range(1, numeros+1):
#     ganador = int(input("Ingresa el " + str(i) + "  numero "))
#     ganadores.append(ganador)

# ganadores.sort()
# ganadores.reverse()
# print(ganadores)



# # Escribir un programa que almacene las asignaturas de un curso
# # (por ejemplo Matem�ticas, F�sica, Qu�mica, Historia y Lengua) en una lista,
# # pregunte al usuario la nota que ha sacado en cada asignatura
# # y elimine de la lista las asignaturas aprobadas.
# # Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# materias = ["Matem�ticas", "F�sica", "Qu�mica", "Historia", "Lengua"]
# ganadas = []
# perdidas = []
# for materia in materias:
#     nota = float(input("�Qu� nota has sacado en " + materia + "?  "))
#     if nota >= 5:
#         ganadas.append(materia)
#     else:
#         perdidas.append(materia)


# for materia in ganadas:
#     materias.remove(materia)

# print(" Lista sin las removidas ", materias)
# print(" Las materias ganadas", ganadas)
# print(" Las materias perdidas", perdidas)

# print("Tienes que repetir " + str(materias))

# # Escribir un programa que almacene el abecedario en una lista,
# # elimine de la lista las letras que ocupen posiciones m�ltiplos de 3,
# # y muestre por pantalla la lista resultante.

# abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# print(abecedario)

# mide = len(abecedario)
# print("len de abecedario  ", mide)

# for i in range(len(abecedario), 1, -1):

#     if i % 3 == 0:
#         abecedario.pop(i-1)

# print(abecedario)


# # pal�ndromo. palabras que se leen igual de derecha a izquierda y de izquierda a derecha. ej anilina, ara�ara


# palabra = input("Introduce una palabra: ")
# palabrainversa = palabra
# palabra = list(palabra)
# print("la palabra ", palabra)
# palabrainversa = list(palabrainversa)
# palabrainversa.reverse()
# print("palabra inversa ", palabrainversa)

# if palabra == palabrainversa:
#     print("Es un pal�ndromo")
# else:
#     print("No es un pal�ndromo")



# # Escribir un programa que pida al usuario una frase
# # y muestre por pantalla el n�mero de veces que contiene cada vocal.

# frase = input("Introduce una palabra: ")
# vocales = ['a', 'e', 'i', 'o', 'u']
# for vocal in vocales:
#     veces = 0
#     for letra in frase:
#         if letra == vocal:
#             veces += 1
#     print("La vocal " + vocal + " aparece " + str(veces) + " veces")


# #Escribir un programa que almacene en una lista los siguientes precios,
# # 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla
# # el menor y el mayor de los precios.

# precios = [50, 75, 46, 22, 80, 65, 8]
# min = max = precios[0]
# for precio in precios:
#     if precio < min:
#         min = precio
#     elif precio > max:
#         max = precio
# print("El m�nimo es " + str(min)) 
# print("El m�ximo es " + str(max))


# # Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2)
# # en dos listas y muestre por pantalla su producto escalar.

# a = (1, 2, 3)
# b = (-1, 0, 2)
# producto = 0
# for i in range(len(a)):
#     producto += a[i]*b[i]
# print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(producto))



# # teniendo una lista con varias listas anidadas de productos, cada una con la siguiente informaci�n
# # Nombre del producto, saldo anterior, precio de compra, porcentaje de utilidad
# # calcular el precio de venta, solictar las compras y las ventas y generar nuevo saldo
# # Actualizar cada una de las listas anidadas con la informaci�n calculada y solicitada


# productos = [["camisas", 10, 15000, 0.4],["zapatos", 30, 50000, 0.6],["blusas", 30, 15000, 0.3],["pantalones", 10, 60000, 0.5]]
# print(productos)
# i = 0
# for i in range(len(productos)):
# #    print(i)
#     pventa = productos[i][2] * productos[i][3] + productos[i][2]
# #    print(pventa)
#     productos[i].append(pventa)
#     compras = int(input("las compras para " + productos[i][0] + " fueron "))
#     ventas = int(input("las ventas para " + productos[i][0] + " fueron "))
#     nsaldo = productos[i][1] + compras - ventas
#     productos[i].append(compras)
#     productos[i].append(ventas)
#     productos[i].append(nsaldo)
# print(productos)

# for i in range(len(productos)):
#     print("Producto: ",productos[i][0], end= " ")
#     print("Saldo Ant: ",productos[i][1], end=" ")
#     print("Precio compra: ",productos[i][2], end=" ")
#     print("Porcentaje Ganancia: ",productos[i][3], end=" ")
#     print("Precio de venta: ",productos[i][4], end=" ")
#     print("Compras: ",productos[i][5], end=" ")
#     print("Ventas: ",productos[i][6], end=" ")
#     print("Nuevo Saldo: ",productos[i][7])


# # capacidad de gastos por estrato
# # cuanto dinero en cada prenda y cuanto dinero en total


# items = ["pantalones", "camisas", "zapatos", "interiores"]

# res1, res2, res3, res4, res5, res6 = [], [], [], [], [], []

# sp1, sp2, sp3, sp4, sp5, sp6 = 0, 0, 0, 0, 0, 0

# sc1, sc2, sc3, sc4, sc5, sc6 = 0, 0, 0, 0, 0, 0

# sz1, sz2, sz3, sz4, sz5, sz6 = 0, 0, 0, 0, 0, 0

# si1, si2, si3, si4, si5, si6 = 0, 0, 0, 0, 0, 0

# for i in range(6):
#     estrato = int(input("Cual es su estrato social? "))
#     pantalones = int(input("El dinero anual que gastaste en " + items[0] + " fue? " ))
#     camisas = int(input("El dinero anual gastaste en " + items[1] + " fue? "))
#     zapatos = int(input("El dinero anual gastaste en " + items[2] + " fue? "))
#     interiores = int(input("El dinero anual gastaste en " + items[3] + "fue? "))
#     if estrato == 1:
#         sp1 = sp1 + pantalones
#         sc1 = sc1 + camisas
#         sz1 = sz1 + zapatos
#         si1 = si1 + interiores

#         res1.append(sp1)
#         res1.append(sc1)
#         res1.append(sz1)
#         res1.append(sz1)

#     if estrato == 2:
#         sp2 =+ pantalones
#         sc2 =+ camisas
#         sz2 =+ zapatos
#         si2 =+ interiores

#         res2.append(sp2)
#         res2.append(sc2)
#         res2.append(sz2)
#         res2.append(sz2)

#     if estrato == 3:
#         sp3 =+ pantalones
#         sc3 =+ camisas
#         sz3 =+ zapatos
#         si3 =+ interiores

#         res3.append(sp3)
#         res3.append(sc3)
#         res3.append(sz3)
#         res3.append(sz3)

#     if estrato == 4:
#         sp4 =+ pantalones
#         sc4 =+ camisas
#         sz4 =+ zapatos
#         si4 = + interiores

#         res4.append(sp4)
#         res4.append(sc4)
#         res4.append(sz4)
#         res4.append(sz4)

#     if estrato == 5:
#         sp5 =+ pantalones
#         sc5 =+ camisas
#         sz5 =+ zapatos
#         si5 = + interiores

#         res5.append(sp5)
#         res5.append(sc5)
#         res5.append(sz5)
#         res5.append(sz5)

#     if estrato == 6:
#         sp6 =+ pantalones
#         sc6 =+ camisas
#         sz6 =+ zapatos
#         si6 = + interiores

#         res6.append(sp6)
#         res6.append(sc6)
#         res6.append(sz6)
#         res6.append(sz6)

#     print(res1, res2, res3)
#     print(res4, res5, res6)
    
    

# lista1 = [12,54,60,27,42,2]
# listap = []
# listap.extend(lista1)
# listama = []
# mayor = 0
# elrango = len(lista1)
# k = elrango
# while k != 0:
#     for i in range(elrango):
#         numero = (lista1[i])
#     #    print(" el leido", numero)
#         if numero > mayor:
#             mayor = numero
#             i = i + 1

#     #print(mayor)
#     listama.append(mayor)
#     lista1.remove(mayor)
#     print("La lista con los mayores uno a uno ",listama)
#     print("La lista con los mayores removidos ",lista1)
#     elrango = len(lista1)
#     mayor = 0
#     k = k - 1


# lista = ["Antioquia", "Medellin", "Bello", "itagui"], ["Cundinamarca", "Bogota", "Chia", "Soacha"], ["Valle", "Cali", "Buga", "Jamundi"]
# for k in range(len(lista)):
#     print(lista[k])
#     for j in range(3):
#         print(lista[k][j])


# lista_numeros = [10, 45, 55, 76]

# print(f"El valor m�s peque�o en la lista es el {lista_numeros[0]}. El m�s grande, el {lista_numeros[3]}.")


# # acceder a un caracter de un elemento de una lista

# lista_colores = ["rojo", "azul", "verde", "amarillo"]

# print(lista_colores[1][2])

# #Primero a�ado "gris" en la posici�n 0. "rosa" lo pongo al final y "naranja" en la posici�n 3.
# lista_colores = ["rojo", "azul", "verde", "amarillo"]

# lista_colores.insert(0,"gris")
# lista_colores.append("rosa")
# lista_colores.insert(3,"naranja")

# print(lista_colores)

# # cuantas veces se encuentra el numero 10

# lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]

# print(lista_numeros.count(10))

# # construir una lista con determinado numero de palabras

# numero = int(input("D�game cu�ntas palabras tiene la lista: "))
# if numero < 1:
#   print("�Imposible!")
# else:
#   lista = []
#   for i in range(numero):
#       palabra = input(f"D�game la palabra {i + 1}: ")
#       lista += [palabra]
#   print(f"La lista creada es: {lista}")



# # buscar una palabra en la lista

# numero = int(input("D�game cu�ntas palabras tiene la lista: "))

# if numero < 1:
#   print("�Imposible!")
# else:
#   lista = []
#   for i in range(numero):
#       palabra = input(f"D�game la palabra {i + 1}: ")
#       lista += [palabra]
#   print(f"La lista creada es: {lista}")

#   buscar = input("D�game la palabra a buscar: ")
#   contador = 0
#   for i in lista:
#       if i == buscar:
#           contador += 1
#   if contador == 0:
#       print(f"La palabra '{buscar}' no aparece en la lista.")
#   elif contador == 1:
#       print(f"La palabra '{buscar}' aparece una vez en la lista.")
#   else:
#       print(f"La palabra '{buscar}' aparece {contador} veces en la lista.")


# # sustituir una palabra en la lista

# numero = int(input("D�game cu�ntas palabras tiene la lista: "))

# if numero < 1:
#   print("�Imposible!")
# else:
#   lista = []
#   for i in range(numero):
#       palabra = input(f"D�game la palabra {i + 1}: ")
#       lista += [palabra]
#   print(f"La lista creada es: {lista}")

#   buscar = input("Sustituir la palabra: ")
#   sustituir = input("por la palabra: ")
#   for i in range(len(lista)):
#       if lista[i] == buscar:
#           lista[i] = sustituir
#   print(f"La lista es ahora: {lista}")


# # eliminar palabras de la lista

# numero = int(input("D�game cu�ntas palabras tiene la lista: "))

# if numero < 1:
#   print("�Imposible!")
# else:
#   lista = []
#   for i in range(numero):
#       palabra = input(f"D�game la palabra {i + 1}: ")
#       lista += [palabra]
#   print(f"La lista creada es: {lista}")

#   eliminar = input("Palabra a eliminar: ")
#   for i in range(len(lista) - 1, -1, -1):
#       if lista[i] == eliminar:
#           del lista[i]
#   print(f"La lista es ahora: {lista}")


# # eliminar elemento repetidos
# numero = int(input("D�game cu�ntas palabras tiene la lista: "))

# if numero < 1:
#     print("�Imposible!")
# else:
#     lista = []
#     for i in range(numero):
#         palabra = input(f"D�game la palabra {i + 1}: ")
#         lista += [palabra]
#     print(f"La lista creada es: {lista}")

#     for i in range(len(lista) - 1, -1, -1):
#         if lista[i] in lista[:i]:
#             del lista[i]
#     print(f"La lista sin repeticiones es: {lista}") """


