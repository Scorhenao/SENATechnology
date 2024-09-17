# Un diccionario es un conjunto de pares clave:valor donde clave es un dato no mutable
# y valor es cualquier tipo de dato.
#
# diccionario = {clave1:valor1, clave2:valor2,....,clavek:valork}

# Un diccionario en Python es una colecci�n de elementos, donde cada uno tiene una llave key y un valor value.
# Los diccionarios se pueden crear con par�ntesis {} separando con una coma cada par.


vacio = {}
print(f" Diccionario vacio {vacio}")

# Diccionarios homogeneo

edades =   {"juan": 26,
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
diclist =   {"a": [1, 2],
            "b" : [0, 1, 2],
            }
print(f" Diccionario de listas {diclist}")

dictupla =  {"a": (1, 2),
            "b" : (0, 1, 2),
            }
print(f" Diccionario de tuplas {dictupla}")

# diccionario con claves numericas

dicnum =   {1: 5,
            4: 7,
            }

print(f" Diccionario con claves numericas {dicnum}")