# factura = [["xxx", "xxxx", "xxx", "xxx"], ["yyy", "yyyy", "yyyy","yyyy"]]
# for elemento in factura:
#     print(elemento)

# print(factura[0])
# print(factura[1])
# print(factura[0][2])



# for element in (1, 2, 3):
#     print(element)
# for key in {'one':1, 'two':2}:
#     print(key)
# for char in "123":
#     print(char)

# lista = [[56, 34, 1],
#          [12, 4, 5],
#          [9, 4, 3]]

# for i in lista:
#     print(i)

# for i in range(0,3):
#     for j in range(0,3):
#         print(lista[i][j], end=" ")#imprimir desde la lista anterior en la misma linea

# #imprime lista completa 3 veces
# for i in range(3):
#     print(lista)

# # recorre por filas y dentro de ella por columnas

# for i in lista:
#     for j in i:
#         print(j)
# # Salida: 56,34,1,12,4,5,9,4,3"""


# print(list(range(5, 20, 2)))# desde el 5 hasta el 20 con incremento de dos crear lista

# a = [1, 2]
# b = ["Uno", "Dos"]
# c = zip(a, b) # fucionar lista de diferentes tipos con key 
# print(list(c))

# Nombres = ["Carlos","Manuel","Diana"]
# Apellidos = ["Montoya","Martinez","Qui�onez"]
# nya = zip(Nombres,Apellidos)
# print(list(nya))


# #
# for numero, texto in zip(a, b):
#     print("N�mero", numero, "Letra", texto)

# # N�mero 1 Letra Uno
# # N�mero 2 Letra Dos

# numeros = [1, 2]
# espanol = ["Uno", "Dos"]
# ingles = ["One", "Two"]
# frances = ["Un", "Deux"]
# c = zip(numeros, espanol, ingles, frances)

# for n, e, i, f in zip(numeros, espanol, ingles, frances):
#     print(n, e, i, f)

# # 1 Uno One Un
# # 2 Dos Two Deux

# lista = ["A", "B", "C"]

# indice = 0
# for l in lista:
#     print(indice, l)
#     indice += 1

# # Salida:
# # 0 A
# # 1 B
# # 2 C

# lista = ["A", "B", "C"]

# for indice, l in enumerate(lista):
#     print(indice, l)

# # Salida:
# # 0 A
# # 1 B
# # 2 C

# #acceder a los �ndices de una colecci�n,
# lista = ["A", "B", "C"]

# en = list(enumerate(lista))
# print(en)

# # Salida;
# # [(0, 'A'), (1, 'B'), (2, 'C')]

# # crear listas de elementos en una misma linea

# cuadrados = []
# for i in range(5):
#     cuadrados.append(i**2)
#     print(cuadrados, (i))
# #[0, 1, 4, 9, 16]

# unos = [1 for i in range(5)]
# print(unos)

# unos = ["Carlos" for i in range(5)]
# print(unos)
# #[1, 1, 1, 1, 1]


# frase = "El perro de san roque no tiene rabo"
# erres = [i for i in frase if i == 'r']
# print(erres)
# #['r', 'r', 'r', 'r']

# print(len(erres))