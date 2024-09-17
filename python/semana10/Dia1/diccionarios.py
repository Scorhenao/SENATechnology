
# Un diccionario es un conjunto de pares clave:valor donde clave es un dato no mutable
# y valor es cualquier tipo de dato.
#
# diccionario = {clave1:valor1, clave2:valor2,....,clavek:valork}

# Un diccionario en Python es una colecci�n de elementos, donde cada uno tiene una llave key y un valor value.
# Los diccionarios se pueden crear con par�ntesis {} separando con una coma cada par.


vacio = {}
print(f" Diccionario vacio {vacio}")

# Diccionarios homogeneo

edades =  {"juan": 26,
            "maria": 19,
            "raquel": 45
            }
print(f" Diccionario homogeneo {edades}")


# diccionario heterogeneo
datosedad = {"nombre": "carlos",
            "apellido" : "Ruiz",
            "edad": 32
            }
print(f" Diccionario de edades {datosedad}")

# diccionario con listas y diccionarios
diclist = {"a": [1, 2],
            "b" : [0, 1, 2],
            }
print(f" Diccionario de listas {diclist}")

dictupla = {"a": (1, 2),
            "b" : (0, 1, 2),
            }
print(f" Diccionario de tuplas {dictupla}")

# diccionario con claves numericas

dicnum =    {1: 5,
            4: 7,
            }

print(f" Diccionario con claves numericas {dicnum}")

# un diccionario no puede tener claves repetidas

otrodict = {"juan": 30,
            "marta": 25,
            "juan": 60
            }

print(f" Diccionario con claves repetidas {otrodict}")
# deja el ultimo elemento

# con distintos tipos de datos. No se debe de hacer. No genera error

condist = {3: 26,
            "nombre": "pedro",
            -2: "hola"
            }

print(f" Diccionario con claves distintos tipos {condist}")


# acceder a los elementos de un diccionario. Se accede a los elementos a trves de sus claves

dicc = {"a": 5,
        "b": 7
        }

valor1 = dicc["a"]
print(valor1)

# Tambien se tienen diccionarios con numeros y grupos

diccionario = {"numeros": [1, 2, 5],
               "grupos": {"a": 1, "b": 2
                }}

valor1 = diccionario["numeros"]
print(valor1)
valor2 = diccionario["grupos"]
print(valor2)
# para acceder al elemento 5 de numeros
valor1 = diccionario["numeros"][2]
print(valor1)
valor1 = diccionario["grupos"]["b"]
print(valor1)
# Cuando la clave no existe en el diccionario
#valor1 = diccionario["grupos"]["d"]
#print(valor1)


print(f"Clave numbers: {diccionario['numeros']}")
print(f"Clave groups: {diccionario['grupos']}")

print(f"Clave numbers: {diccionario['numeros'][1]}")
print(f"Clave groups: {diccionario['grupos']['b']}")



# metodos
# items me entrega una lista de tuplas

diccionario = {"numeros": [1, 2, 5],
               "grupos": {"a": 1, "b": 2
                }}

print(diccionario.items())

a = {"a": 1, "b": 8, "c": 12}
print("Los items de a ",a.items())

# para sacar la list de elementos - Constructor list

lista = list(diccionario.items())
print("Lista con los items del diccionario ",lista)

elemento = lista[1]
print(elemento)

# metodo keys. Devuelve en una lista todas las claves del diccionario

diccionario = {"numeros": [1, 2, 5],
               "grupos": {"a": 1, "b": 2
                }}

print("Las claves del diccionario ",diccionario.keys())
lista = list(diccionario.keys())
print(lista)

print("Los valores del diccionario ",diccionario.values())
lista = list(diccionario.values())
print(lista)
print(lista[0][0])
lista2 = list(lista[1])
print(lista2)
print(lista2[0])







horario = {'lunes':'11:30', 'martes':'8:30', 'mi�rcoles':'8:30',  'viernes':'11:30'}
print(horario)

clases = {'lunes':['11:30','IAL'], 'martes':['8:30','IAG'], 'mi�rcoles':['8:30','IAL'],  'viernes':['11:30','IAG']}

dvacio = {}

# se itera los elementos con las claves

#for u in horario:
#    print(u)

# otra forma

#for u in horario.keys():
#    print(u)

for u in clases:
    print(u)

# genera dos iterables


# forma de generar un diccionario con las claves o elementos y sus valores

letras = dict(zip('abcdef', list(range(6))))
print(letras)

L1 = ['La Mari', 'La Paqui', 'La Juani']
L2 = [24,26,31]
edad = dict(zip(L1,L2))
print(edad)

L1 = ['Carlos', 'Libardo', 'Carlos Manuel']
L2 = ['Montoya', 'rend�n', 'Montoya']
nombyape = dict(zip(L1,L2))
print(nombyape)

# len o longitud es la cantidad de pares de claves y valores
print(len(nombyape))

# aplicar con nombres y salarios, codigo y producto, materia y calificacion, etc

# Se pueden a�adir nuevos elementos o cambiar los valores de las claves:
#
# diccionario[clave] = valor

letras = dict(zip('abcdef', list(range(6))))
letras['g'] = 6
letras["h"], letras["i"] = 7, 8
print(letras)

# modificar par clave:valor
letras['a'] = 1
print(letras)

patas = {}

patas['gallina'] = 2
patas['vaca'] = 4
patas['rana'] = 4
patas['pulpo'] = 8
patas['mosca'] = 6
patas['ara�a'] = 8
patas['cigala'] = 10

print(patas)

d3 = dict(Nombre='Sara',
          Edad=27,
          Documento=1003882, salario=120000, cargo= "auxiliar")
print(d3)

print(d3['Nombre'])     #Sara
print(d3.get('Edad')) #Sara

d3["Nombre"] = "Laura"
print(d3['Nombre'])

# para imprimir las claves del diccionario se interan o recorren

for i in d3:
    print(i)


# Para imprimir los valores

for x in d3:
    print(d3[x])

# para imprimir las claves y valores a la vez

d3 = dict(Nombre='Sara',
          Edad=27,
          Documento=1003882, salario=120000, cargo= "auxiliar")

for x, y in d3.items():
    print(x, y)


#Los diccionarios en Python pueden contener uno dentro de otro. Podemos ver como los valores anidado uno y dos del
#diccionario d contienen a su vez otro diccionario.

anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
  "anidado1" : anidado1,
  "anidado2" : anidado2
}
print(d)

#El m�todo clear() elimina todo el contenido del diccionario.

d = {'a': 1, 'b': 2}
d.clear()
print(d) #{}

# El m�todo get() nos permite consultar el value para un key determinado.

d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado'))

# El m�todo items() devuelve una lista con los keys y values del diccionario.

d = {'a': 1, 'b': 2}
it = d.items()
print(it)             #dict_items([('a', 1), ('b', 2)])
print(list(it))       #[('a', 1), ('b', 2)]
print(list(it)[0][0]) #a

# El m�todo keys() devuelve una lista con todas las keys del diccionario.

d = {'a': 1, 'b': 2}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']

# El m�todo values() devuelve una lista con todos los values o valores del diccionario.

d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]
print(tuple(d.values())) #[1, 2]

# El m�todo pop() busca y elimina la key que se pasa como par�metro y devuelve su valor asociado.

d = {'a': 1, 'b': 2}
d.pop('a')
print(d) #{'b': 2}
#d.pop('z')
print(d) #{'b': 2}


d = {'a': 1, 'b': 2}
d.pop('c', -1)
print(d) #{'a': 1, 'b': 2}

# El m�todo popitem() elimina de manera aleatoria un elemento del diccionario.

d = {'a': 1, 'b': 2,"c":10, "e":20}
d.popitem()
print(d)
#{'a': 1}


d = {'a': 1, 'b': 2,"c":10, "e":20}
d.popitem()
print(d)
#{'a': 1}



# El m�todo update() se llama sobre un diccionario y tiene como entrada otro diccionario. Los value son actualizados
# y si alguna key del nuevo diccionario no esta, es a�adida.

d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)
print(d1)"""