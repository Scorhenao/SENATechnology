# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas
# # claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.



"""numero = int(input("Dime un número:"))
cuadrados = {}

for num in range(1,numero+1):
# instruccion para hacer una lista
    cuadrados[num] = num ** 2
# se hace un recorrido a la par
for num, valor in cuadrados.items():
    print("%d -> %d" % (num,valor))

# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada
carácter en la cadena.

dict = {}
cadena = input("Dame una cadena:")
for caracter in cadena:
	if caracter in dict:
		dict[caracter]+=1
	else:
		dict[caracter]=1

for campo,valor in dict.items():
	print (campo,"->",valor)



# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar
# los precios de las distintas frutas. El programa pedirá el nombre de la fruta
# y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir
# de los datos guardados en el diccionario. Si la fruta no existe nos dará un error.
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

precios = {"manzana": 2, "naranja": 1.5, "platano": 4, "piña": 3}
while True:
    fruta = input("Dime la fruta que has vendido:")
    if fruta.lower() not in precios:
        print("Fruta no existe.")
    else:
        cantidad = int(input("Dime la cantidad de frutas que has vendido:"))
        print("El precio es de %f" % (cantidad * precios[fruta]))
    opcion = input("¿Quieres vender otra fruta (s/n)")
    while opcion.lower() != "s" and opcion.lower() != "n":
        opcion = input("¿Quieres vender otra fruta (s/n)")
    if opcion.lower() == "n":
# Opcion que aborta el while true
        break


# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase
# y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas.
# Guarda la información en un diccionario cuya claves serán los nombres de los alumnos
# y los valores serán listas con las notas de cada alumno.

# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá
# pidiendo sus notas hasta que introduzcamos un número negativo.
# Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
# Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guradar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    notas=[]
    nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    alumnos[alumno] = notas.copy()

for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f" % (alumno,sum(notas)/len(notas)))

# Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono.
# El programa nos dará el siguiente menú:
#
# * Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y,
# opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe
# permitir ingresar el teléfono correspondiente.
# * Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# * Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# * Listar: Nos muestra todos los contactos de la agenda.
#
# Implementar el programa con un diccionario.

agenda = {}
while True:
    print("\n")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")

    opcion = int(input("Dime opción:"))
    if opcion == 1:
        nombre = input("Nombre del contacto:")
        if nombre in agenda:
            print("%s ya existe su número de teléfono es %s" % (nombre, agenda[nombre]))
            opcion = input("Pulsa 's' si quieres modificarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                numero = input("Dame el nuevo número de teléfono:")
                agenda[nombre] = numero
        else:
            numero = input("Dame el número de teléfono:")
            agenda[nombre] = numero
    elif opcion == 2:
        cadena = input("Nombre del contacto a buscar:")
        for nombre, numero in agenda.items():
            if nombre.startswith(cadena):
                print("El número de teléfono de %s es el %s" % (nombre, agenda[nombre]))
    elif opcion == 3:
        nombre = input("Nombre del contacto para borrar:")
        if nombre in agenda:
            opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                del agenda[nombre]
        else:
            print("No existe el contacto")
    elif opcion == 4:
        for nombre, numero in agenda.items():
            print(nombre, "->", numero)
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")



# Genera diccionario con claves desde 1 al numero y sus valor el numero leido * 3

numero = int(input("Dime un número:"))
cubos = {}
# defino elementos a meter
for num in range(1,numero+1):

# aqui s va generando el diccionario

    cubos[num] = num ** 3
# se hace un recorrido a la par
for num, valor in cubos.items():
# la instruccion en comillas, los % y de permiten escribir los valores
    print("%d -> %d" % (num,valor))

persona1 = {"Nombre":"Carlos","Apellido":"montoya","Cedula":"70104641","Edad":30, "Sexo":"m"}
# el tamaño es el numero de items o el par clave : Valor
print(len(persona1))

print(persona1)
print(persona1["Nombre"])
print(persona1["Apellido"])
print(persona1["Cedula"])
print(persona1["Edad"])
print(persona1["Sexo"])

print("sus claves ", persona1.keys())
print("sus items ", persona1.items())
# los muestra como una lista con cada uno de sus pares como tuplas

apellido = input("ingrese un Apellido ")

if apellido in persona1:
    print("existe Apellido ", True)
else:
    print("eNo xiste Apellido ", False)

persona2 = dict(Nombre = "Maria Cecilia", Apellido = "Rincon", Cedula = "456145", Edad = 27, Sex0 = "f" )
print(persona2)

print("sus valores ", persona2.values())

# para acceder a cierto valor
print("persona 2", persona2["Apellido"])

nombre = input("ingrese un Nombre ")
#for nombre in persona2:
if nombre in persona2:
    print("existe en nombre ",True)
else:
    print(False)

listap = ["carlos","ramiro","pedro", "carlos", "jose", "marta", "carlos"]
unicos = dict.fromkeys(listap)
print("Las claves  ",unicos.keys())
print("Los valores ", unicos.values())
print("Los items ", unicos.items())
nombresunicos = list(unicos)
print(nombresunicos)

# recuerde que las claves no se pueden repetir


letras = list(dict.fromkeys("con la lista de letras de esta frase hago un diccionario"))
print(letras)"""



