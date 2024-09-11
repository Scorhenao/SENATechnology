#Convierte la siguiente lista en una tupla
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores_tupla = tuple(colores)

print(colores_tupla)


colores = ('rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja')

colores_lista = list(colores)

print(colores_lista)

#EJERCICIO 01 Escribir un programa que lea en una lista n nombres de paises, luego lo convierta a una tupla
# y muestre dichos paises.

# paises = []

# for i in range(3):
#     pais = input("Ingresa un pais: ")
#     paises.append(pais)
#     paises_tupla = tuple(paises)
#     print(f"Los paises ingresados son: {paises_tupla}")


# EJERCICIO 02 Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matem�ticas, F�sica,Qu�mica,
# Historia y Lengua) en una tupla, luego pida la nota final de cada curso y muestre porpantalla el
# mensaje el promedio obtenido por el estudiante.

# cursos = (
#     "Matematicas",
#     "Fisica",
#     "Quimica",
#     "Historia",
#     "Lengua"
# )

# for i in range(3):
#     estudiante = input("Ingresa el nombre del estudiante: ")
    
#     notas = []
#     for curso in cursos:
#         print(cursos)
#         notafinal = float(input(f"Ingresa la nota final del estudiante {estudiante} en el curso {curso}: "))

#         validacion = "Nota no valida" if notafinal < 0 or notafinal > 5 else f"la nota: {notafinal} se ha agregado exitosamente al curso: {curso}"
#         print(validacion)
#         if validacion == "Nota no valida":
#             exit()

#         notas.append(notafinal)

#         cantidadDeNotas = len(notas)
#         sumaDeNotas = sum(notas)
#         promedio = sumaDeNotas / cantidadDeNotas
#     print(cantidadDeNotas)
#     print(sumaDeNotas)
#     print(promedio)
#     print(f"El promedio del estudiante {estudiante}  es: {promedio}")

# EJERCICIO 03 Escribir un programa que contenga los dias de la semana en una tupla, pide numeros al usuario,
# siel numero esta entre 1 y la longitud maxima de la tupla, muestra el contenido de esa posicion sinomuestra
# un mensaje de error. El programa termina cuando el usuario ingresa el valor cero = 0

# meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre","Diciembre")

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


# EJERCICIO 04 Construir un programa que pide numeros y metelos en una lista, cuando el usuario meta un 0
# dejade insertar, lo convierta en una tupla y muestre el mayor, menor valor y la tupla ordenada.

# numeros = []

# while True:
#     numero = int(input("Ingresa un numero (0 para salir): "))
#     if numero == 0:
#         break
#     numeros.append(numero)

# numeros_tupla = tuple(numeros)
# print("La tupla es:", numeros_tupla)

# print("El mayor numero es:", max(numeros_tupla))
# print("El menor numero es:", min(numeros_tupla))

# numeros_ordenados = sorted(numeros_tupla)
# print("La tupla ordenada es:", numeros_ordenados)


# EJERCICIO 05 Construir un programa que inicialice una tupla con numeros, luego pida un numero por teclado
# e indica cuantas veces se repite ese numero en la tupla

# numeros = (5, 4, 3, 2, 1, 6, 45, 3, 6, 6, 6, 6, 6)

# while True:
#     numero = int(input("Ingresa un numero (0 para salir): "))
#     if numero == 0:
#         break

#     if numero in numeros:
#         print(f"La tupla tiene {numeros.count(numero)} veces el numero {numero}.")
#         print(f"La tupla es: {numeros}")
