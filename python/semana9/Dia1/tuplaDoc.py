#!/usr/bin/python3

# Ejercicio sobre el uso de tuplas en Python.
# Una tupla es una estructura de datos inmutable, lo que significa que no se puede modificar 
# después de su creación (a diferencia de las listas). A continuación, se presentan diversos 
# ejemplos y ejercicios para trabajar con tuplas.

# Creación de una tupla básica con diferentes tipos de datos
tupla = (70104641, "Carlos Montoya", 6000000)
print(tupla)

# Creación de una tupla vacía
tuplavacia = ()
print(tuplavacia)

# Creación de una tupla con un solo elemento. Es importante recordar que debe tener una coma al final.
tupladeuno = (3,)
print(tupladeuno)

# Acceso a los elementos de la tupla por índice
eluno = tupla[0]  # Primer elemento
eldos = tupla[1]  # Segundo elemento
eltres = tupla[2]  # Tercer elemento

# Imprimiendo elementos individuales de la tupla
print("El primer elemento es:", eluno)
print("El último elemento es:", tupla[-1])  # Último elemento utilizando índice negativo

# Longitud de la tupla (número de elementos)
print("Longitud de la tupla:", len(tupla))

# Recorrer una tupla con un bucle for
for t in tupla:
    print(t)

# Slicing (subconjuntos de tupla)
tupla = ("a", "b", "c", "d", "e", "f")
tupla2 = tupla[1:3]  # Subtupla desde el segundo al tercer elemento
print(tupla2)

tupla3 = tupla[:3]  # Subtupla desde el primer elemento hasta el tercero
print(tupla3)

tupla4 = tupla[1:]  # Subtupla desde el segundo elemento hasta el final
print(tupla4)

# Concatenación de tuplas (unión de varias tuplas)
tutodas = tupla + tupla2 + tupla3
print(tutodas)

# Métodos de las tuplas
# Contar cuántas veces aparece un elemento en la tupla
print("Cantidad de veces que aparece 'b':", tutodas.count("b"))

# Obtener la posición de un elemento en la tupla
t1 = (1, 3, 8, 5, 2)
a = t1.index(8)  # Primera aparición del valor 8
print("Posición de 8 en la tupla:", a)

# Buscar un elemento con un rango de búsqueda (índice inicial y final)
b = t1.index(5, 0, 4)  # Busca el número 5 entre las posiciones 0 y 4
print("Posición de 5 en el rango:", b)

# Obtener la longitud de una tupla
print("Longitud de la tupla:", len(t1))

# Obtener el valor máximo y mínimo de una tupla
print("Valor máximo:", max(t1))
print("Valor mínimo:", min(t1))

# Sumar todos los elementos de una tupla (solo si son numéricos)
print("Suma de todos los elementos de t1:", sum(t1))

# Desempaquetado de tuplas: asignar los valores de la tupla a varias variables
datos_ciudad = ('Valladolid', 'Castilla y León', 'España')
ciudad, comunidad, pais = datos_ciudad
print(f'Ciudad: {ciudad}\nComunidad: {comunidad}\nPaís: {pais}')

# Trabajando con rangos y tuplas
r = range(1, 10, 2)  # Rango de números impares entre 1 y 9
print(r.start, r.stop, r.step)

# Crear listas y tuplas a partir de rangos
lista = list(range(10))  # Lista de números del 0 al 9
print("Lista creada con range(10):", lista)

tupla = tuple(range(5, 15))  # Tupla con números del 5 al 14
print("Tupla creada con range(5, 15):", tupla)

lista = list(range(4, 21, 2))  # Lista de números pares entre 4 y 20
print("Lista creada con range(4, 21, 2):", lista)

tupla = tuple(range(3, -13, -3))  # Tupla de números con paso negativo
print("Tupla creada con range(3, -13, -3):", tupla)

# Ejercicio: intercambiar los valores de dos variables a y b
a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))

# Método clásico para intercambiar valores
x = a
a = b
b = x
print(f"Valores intercambiados (método clásico): a = {a}, b = {b}")

# Método más eficiente usando tuplas
a, b = b, a
print(f"Valores intercambiados (usando tuplas): a = {a}, b = {b}")
