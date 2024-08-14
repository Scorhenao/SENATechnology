# leer los elementos de una lista con nombre, edad y salario
lista = ["sam", 27, 2.000000]


# lista en blanco
y=[]
print(y)

# lectura de los elementos de izquierda a derecha basado en su indice

eluno=lista[0]
print(f"El primer elemento de la lista lista es: {eluno}")
eldos=lista[1]
print( f"El segundo elemento de la lista lista es: {eldos}")
eltres=lista[2]
print(f"El tercer elemento de la lista lista es: ${eltres}")

# lectura de derecha a izquierda
reluno=lista[-1]
print(f"El tercer elemento de la lista lista es: ${reluno}")
reldos=lista[-2]
print(f"El segundo elemento de la lista lista es: {reldos}")
reltres=lista[-3]
print(f"El primer elemento de la lista lista es: {reltres}")

# recorrer lista con un for
for i in lista:
    print(i)

# concatenar listas
a = [1,2,3]
b = [4,5,6]
c = a + b
print(f"""
La concatenacion de las listas a y b es: 
{c}
""")

# repetir la creacion de una lista
d = [0] * 4
print(f"""
La repeticion de la lista d es: 
{d}
""")

f = [1,2,3] * 3
print(f"""
La repeticion de la lista f es: 
{f}
""")

f = f*2
print(f"""
La repeticion de la lista f luego de ya ser repetida es: 
{f}
""")


# rebanar listas

ls=["a","b","c","d","e","f"]
# rebanar los elementos 1 y 2

lsr1 = ls[1 : 3]
print(f"""
la lista ls es:
{ls}
""")
print(f"""imprimir solo los elementos entre los indices 1 al 3
{lsr1}
""")

# rebanar el elemento 3 y 4
lsr2=ls[3:5]
print(f"""
la lista ls es:
{ls}
""")
print(f"""
imprimir solo los elementos entre los indices 3 al 5
{lsr2}
""")

# rebanar el elemento 1
lsr3=ls[0:1]
print(f"""
la lista ls es:
{ls}
""")
print(f"""
imprimir solo los elementros entre los indices 0 al 1
lsr3
""")

# rebanar el elemento 0 y 1
lsr4=ls[0:2]
print(f"""
la lista ls es:
{ls}
""")
print(f"""
imprimir solo los elementos entre los indices 0 al 1
{lsr4}
""")

# rebanar hasta el 4 elemento
lsr5=ls[:4]
print(f"""
la lista ls es:
{ls}
""")
print(f"""
imprimir solo los elementos hasta el indice 4
{lsr5}""")

# rebanar desde el 2 elemento
lsr6=ls[2:]
print(f"""
la lista ls es:
{ls}
""")
print(f"""
imprimir solo los elementos desde el indice 2
{lsr6}""")

# metodos de listas

# adicionar elementos al final de la lista

ls.append("z")
print(f"""
agregando z a la lista
{ls}""")

ls.append("p")
print(f"""
agregando p a la lista
{ls}""")

# extend

ls1=["a","b","c"]
ls2=["d","e","f"]
ls1.extend(ls2)
print(f"""
agregando ls2 a ls1
{ls1}""")

ls2.extend(ls1)
print(f"""
agregando ls1 a ls2 modificada
{ls2}""")


# ordenar listas

ls=[98,56,3,0,1,4,-1]
print(f"""
la lista ls es:
{ls}""")
ls.sort()
print(f"""
la lista ls ordenada es:
{ls}""")


# reversar o voltear listas
ls=[5,2,0,8,-2]
print(f"""
la lista ls es:
{ls}""")
ls.reverse()
print(f"""
la lista ls volteada es:
{ls}""")

#count
#cuenta el numero de ocurrencias de un elemnto
# el 4 tiene 2 ocurrencias


ls=[-1,0,1,3,4,56.98,4]
a=ls.count(4)
print(f"""
la lista ls es:
{ls}""")
print(f"""
la cantidad de ocurrencias del elemento 4 es:
{a}""")

# en que poscicion de la lista se encuentra el elemento 1

ls=[-1,0,1,3,8,56,98,4]
print(f"""
la lista ls es:
{ls}""")
a=ls.index(1,1) # primero el elemento a buscar, el segundo desde donde empieza a buscar
print(f"""
la posicion del elemento 1 es:
{a}""")

numeros = [1, 2, 2, 3, 9, 5, 6, 10]
palabras = ["Yo", "amo", "Python", "Yo", "amo"]
print(f"""
la lista numeros es:
{numeros}""")
#para hallar el indice del elemento 9
#4
indiceDe9 = numeros.index(9)
print(f"""
la posicion del elemento 9 es:
{indiceDe9}
""")
    
indiceDe2 = numeros.index(2) 
print(f"""
la posicion del elemento 2 es:
{indiceDe2}
""")
    
palabraYo = palabras.index("Yo")
print(f"""
la posicion de la palabra Yo es:
{palabraYo}
""")

#print(palabras.index("soy"))

# Insertar elementos en una determinada posicion

ls=[-1,0,1,3,4,56,98,47]
print(f"""
la lista ls es:
{ls}""")
ls.insert(2,899) # primero la posicion, segundo el valor
print(f"""
la lista ls insertando 899 en la posicion 2 es:
{ls}""")

# borrar elementos de la lista basado en el index
ls=[9,569,71,-2,76.5,102]
print(f"""
la lista ls es:
{ls}""")
e=ls.pop(4) # posicion de elemento a borrar
print(f"""
la lista ls borrando el elemento en la posicion 4 es:
{e}""")
print(f"""
la lista ls luego del pop es:
{ls}""")


#remove
ls=[9,569,71,-2,76.5,102]
print(f"""
la lista ls es:
{ls}""")
ls.remove(76.5)
print(f"""
la lista ls borrando el elemento 76.5 es:
{ls}""")

# Ejercicio

# sumar listas
suma1 = 0
suma2 = 0
suma3 = 0
suma4 = 0
suma5 = 0
sumadp = 0
sumads = 0

sumac1 = 0
sumac2 = 0
sumac3 = 0
sumac4 = 0
sumac5 = 0

# hallar el index de un elemento

lista1 = [2, 1, 1, 1, 1]
lista2 = [2, 2, 2, 1, 2]
lista3 = [3, 3, 2, 3, 3]
lista4 = [4, 1, 4, 2, 4]
lista5 = [1, 5, 1, 1, 2]
a = lista3.index(2)
print("valor en el indice 2 lista3 ", a)

# sumando las filas
i = 0
for i in range(len(lista1)):
    suma1 = suma1 + lista1[i]
    suma2 = suma2 + lista2[i]
    suma3 = suma3 + lista3[i]
    suma4 = suma4 + lista4[i]
    suma5 = suma5 + lista5[i]
    i = + 1

print(f"""
la suma de la lista lista1
{suma1}""")
print(f"""
la suma de la lista lista2
{suma2}""")
print(f"""
la suma de la lista lista3
{suma3}""")
print(f"""
la suma de la lista lista4
{suma4}""")
print(suma5)

# sumar diagonal principal
sumadp = lista1[0] + lista2[1] + lista3[2] + lista4[3] + lista5[4]
sumads = lista1[4] + lista2[3] + lista3[2] + lista4[1] + lista5[0]

print(sumadp)
print(sumads)



# sumando las columnas

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

sumasc = []
i = 0
for i in range(len(lista1)):
    sumac1 = lista1[i] + lista2[i] + lista3[i]  + lista4[i]  + lista5[i]
#    print(sumac1)
    sumasc.append(sumac1)
    i = + 1
print(sumasc)

