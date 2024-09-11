# """tupla = (70104641, "Carlos Montoya", 6000000)
# print(tupla)

# tuplavacia = ()
# print(tuplavacia)

# tupladeuno = (3,)
# # hay que colocar la coma para que se considere una tupla y no un 3
# print(tupladeuno)

# eluno = tupla[0]
# eldos = tupla[1]
# eltres = tupla[2]

# print("el uno ", eluno)
# print("el ultimo ", tupla[-1])
# #print("el tres ", eltres)
# # longitud de la tupla
# len(tupla)
# print(len(tupla))
# # recorrer la tupla
# for t in tupla:
#     print(t)

# tupla = ("a", "b", "c", "d", "e", "f")
# tupla2 = tupla[1:3]
# print(tupla2)
# tupla3 = tupla[:3]
# print(tupla3)

# tupla4 = tupla[1:]
# print(tupla4)
# # concatenacion
# tutodas = tupla + tupla2 + tupla3
# print(tutodas)

# # metodos de tuplas
# # contar elementos dentro de la tupla
# print(tutodas.count ("b"))

# t1 = (1,3,8,5,2)
# # la poscicion de la primera ocurrencia del elemento
# a = t1.index(8)
# print("valor de a ",a)
# # un elemento, para inciar busqueda en y terminar en
# b= t1.index(5,0,4)
# print("valor de b ", b)

# mide = len(t1)
# print("Longitud ",mide)
# mayor = max(t1)
# print(mayor)
# menor = min(t1)
# print(menor)
# # suma los elementos de la tupla
# sumar = sum(t1)
# print(sumar)

# #Desempaquetado de una tupla
# #Los elementos de una tupla se pueden asignar a tantas variables como elementos haya en la misma en un proceso llamado desempaquetado (unpacking).

# datos_ciudad = ('Valladolid', 'Castilla y Le�n', 'Espa�a')
# ciudad, comunidad, pais = datos_ciudad
# print(f'Ciudad: {ciudad}\nComunidad: {comunidad}\nPa�s: {pais}')

# r = range(1, 10, 2)
# print(r.start, r.stop, r.step)

# #Listas y tuplas a partir de rangos
# #Como hemos visto para listas y tuplas vac�as, tanto las listas como las tuplas
# # tienen constructores, list() y tuple(). Estos constructores admiten un rango como par�metro para ser creadas. Ve�moslos en acci�n.

# # Enteros del 0 al 9
# lista = list(range(10))
# print("Lista construida con range(10):\n  {}".format(lista))
# # Enteros del 5 al 14
# tupla = tuple(range(5, 15))
# print("Tupla construida con range(5, 15):\n  {}".format(tupla))
# # Pares del 4 al 20
# lista = list(range(4, 21, 2))
# print("Lista construida con range(4, 21, 2):\n  {}".format(lista))
# # Secuencia del 3 al -12 en pasos de -3
# tupla = tuple(range(3, -13, -3))
# print("Tupla construida con range(3, -13, -3):\n  {}".format(tupla))"""


# talleres
# Crea una tupla con los meses del a�o, pide n�meros al usuario, si el numero esta entre 1 y la longitud m�xima de la tupla, muestra el contenido de esa posici�n sino muestra un mensaje de error.
#
# El programa termina cuando el usuario introduce un cero.

# meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
#         "Diciembre")

# salir = False
# while (not salir):

#     numero = int(input("Dame un numero: "))

#     if (numero == 0):
#         salir = True
#     else:
#         if (numero >= 1 and numero <= len(meses)):
#             print(meses[numero - 1])
#         else:
#             print("Inserta un numero entre 1 y ", len(meses))


# Crea una tupla con n�meros, pide un numero por teclado e indica cuantas veces se repite.

# numeros = (5, 4, 3, 2, 1, 6, 45, 3, 6, 6, 6, 6, 6)

# numero = int(input("Dame un numero: "))

# contador = 0
# for i in numeros:
#     if numero == i:
#         contador = contador + 1

# print("Hay ", contador, " repeticion/es")

# # Crea una tupla con n�meros e indica el numero con mayor valor y el que menor tenga.

# numeros = (5, 4, 3, -2, 1, 6, 455, 3, 6, 6, 6, 6, 6)

# maximo = numeros[0]
# minimo = numeros[0]

# for i in numeros:
#     if i > maximo:
#         maximo = i

#     if i < minimo:
#         minimo = i

# print("El maximo es ", maximo)
# print("El minimo es ", minimo)

# # otra forma


# numeros = (7, 6, 5, 4, 3, 2, 3, 4, 5, 1, 4, 3)

# print("Maximo: ", max(numeros))

# print("Minimo: ", min(numeros))

# #  Crea una tupla con valores ya predefinidos del 1 al 10, pide un �ndice por teclado y muestra los valores de la tupla.

# tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# indice = int(input("Dame un indice: "))

# if indice >= 0 and indice < len(tupla):
#     print(tupla[indice])
# else:
#     print("Indice no valido")

# algunos_animales = ("perro", "gato", "rat�n", "serpiente", "caballo")
# todos_los_animales = algunos_animales + ("h�mster", "jirafa")
# print(todos_los_animales)

# # convertir tupla en lista

# animales = ("perro", "gato", "rat�n", "serpiente", "caballo")
# lista_animales = list(animales)
# lista_animales[2] = "elefante"
# print(lista_animales)

# # convertir lista en tupla

# lista_colores = ["azul", "rojo", "amarillo", "naranja"]
# colores = tuple(lista_colores)
# print(colores)
# print(type(colores))

# # eliminar tupla

# animales = ("perro", "gato", "rat�n", "serpiente", "caballo")
# del animales

# # la funcion index

# animales = ("perro", "gato", "rat�n", "serpiente", "caballo")
# print(animales.index("serpiente"))

# # la funcion count

# animales = ("perro", "gato", "rat�n", "serpiente", "caballo","perro","perro")
# print(animales.count("perro"))

# # saber si un elemento existe en la tupla

# colores = 'azul', 'blanco', 'negro'
# if 'azul' in colores:
#     print('S�')
# if 'verde' not in colores:
#     print('No')

# t = (2, 3., 'abd', [3, True], (4,), (4.7, 'a'), ())
# print(t)


# a = 3, True
# print(a)

# x = 3
# y = 5.8
# z = 23
# t1 = x, y, x
# print(t1)

# # desempaquetar valores

# t2 = (4.5, 7.2, 3.)
# u, v, w = t2
# print(u)
# print(w)


# # ordenasr cadenas, listas y tuplas
# # Esta funci�n convierte el objeto en una lista y despu�s la ordena. La lista resultante estr� formada por
# # objetos del mismo tipo.

# c3 = 'ceha4'
# sorted(c3)
# print(c3)
# t3 = (15, 4, 7, 8, 10, 0)
# t4 = ('a', 'We', 'hn', '12')
# l3 = [15, 4, 7, 8, 10, 0.3]
# l4 = ['a', 'We', 'hn', '12']

# (sorted(c3), sorted(t3), sorted(t4), sorted(l3), sorted(l4))
# print(c3,t3,t4,l3,l4)
# """


# #Ejercicio para resolver

# # crear programa que intercambie los valores de a  b

# """a = int(input())
# b = int(input())

# x = a
# a = b
# b = x
# print(a,b)

# (b, a) = (a, b)

# print(a,b)

# # Crea una tupla con los meses del a�o, pide n�meros al usuario, si el numero esta entre 1 y la longitud m�xima de la
# # tupla, muestra el contenido de esa posici�n sino muestra un mensaje de error.

# meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
#          "Diciembre")

# salir = False
# #while (not salir):
# while salir != True:

#     numero = int(input("Dame un numero: "))

#     if (numero == 0):
#         salir = True
#     else:
#         if (numero >= 1 and numero <= len(meses)):
#             print(meses[numero - 1])
#         else:
#             print("Inserta un numero entre 1 y ", len(meses))



# # Crea una tupla con n�meros, pide un numero por teclado e indica cuantas
# #veces se repite

# numeros = (5, 4, 3, 2, 1, 6, 45, 3, 6, 6, 6, 6, 6)

# numero = int(input("Dame un numero: "))

# contador = 0
# for i in numeros:
#     if numero == i:
#         contador = contador + 1

# print("Hay ", contador, " repeticion/es")

# # otra forma

# numeros = (7, 6, 5, 4, 3, 2, 3, 4, 5, 1, 4, 3)

# numero = int(input("Dame un numero: "))

# print("Numero de repeticiones: ", numeros.count(numero))

# # Crea una tupla con n�meros e indica el numero con mayor valor y el que menor tenga.

# numeros = (5, 4, 3, -2, 1, 6, 455, 3, 6, 6, 6, 6, 6)

# maximo = numeros[0]
# minimo = numeros[0]

# for i in numeros:
#     if i > maximo:
#         maximo = i

#     if i < minimo:
#         minimo = i

# print("El maximo es ", maximo)
# print("El minimo es ", minimo)

# # otra forma

# numeros = (7, 6, 5, 4, 3, 2, 3, 4, 5, 1, 4, 3)

# print("Maximo: ", max(numeros))

# print("Minimo: ", min(numeros))

# #Crea una tupla con valores ya predefinidos del 1 al 10, pide un �ndice por teclado y muestra
# # los valores de la tupla.

# tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# indice = int(input("Dame un indice: "))

# if indice >= 0 and indice < len(tupla):
#     print(tupla[indice])
# else:
#     print("Indice no valido")


# tupla = ("naranja", 500,2.5, [3,2,1], "mula")
# a = tupla[3][1]
# print(a)



# #def cargar_fecha():
# dd=int(input("Ingrese numero de dia:"))
# mm=int(input("Ingrese numero de mes:"))
# aa=int(input("Ingrese numero de a�o:"))
# fecha = (dd, mm, aa)
# #    return (dd,mm,aa)


# #def imprimir_fecha(fecha):
# print(fecha[0],fecha[1],fecha[2],sep="/")


# # bloque principal

# #fecha=cargar_fecha()
# #imprimir_fecha(fecha)



# #Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista. Modificar
# # la lista y luego convertir la lista en tupla.


# tupla1 = (25, 12, 2016)
# lista1 = list(tupla1)
# print(tupla1, lista1)
# lista1[0]=31
# print("Imprimimos la lista ya modificada")
# print(lista1)
# tupla2=tuple(lista1)
# print("Imprimimos la segunda tupla que se le copio la lista")
# print(tupla2) 


# # con las tuplas no se pueda el sort, el append y el reverse

# (x, y) = (4, 'fred')
# print(y)
# (a, b) = (99, 98)
# print(a)


# if (0, 1, 2) < (5, 1, 2):
#     print(True)
# if (0, 1, 2000000) < (0, 3, 4):
#     print(True)
# if ( 'Jones', 'Sally' ) < ('Jones', 'Sam'):
#     print(True)
# if ( 'Jones', 'Sally') > ('Adams', 'Sam'):
#     print(True)

# lista = ['rojo', 'azul', 'verde', 'amarillo']
# tupla = tuple(lista)
# print(tupla)

# tupla = ('rojo', 'azul', 'verde', 'amarillo')
# lista = list(tupla)
# print(lista)

# tupla = (10, 15, 20, 'El resultado de la operaci�n es:')
# print(tupla[3], tupla[2] + tupla[0] * tupla[1] / tupla[0])

# # Utiliza los s�mbolos de suma y resta para obtener el resultado 25 a partir de los elementos de la siguiente tupla
# # en una variable llamada operacion

# numeros = (10, 1, 5, 11)
# operacion = numeros[0] + numeros[2] + numeros[3] - numeros[1]
# print(operacion)
# """


