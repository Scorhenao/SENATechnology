import random
lista = []
cuadrados = []
cubos = []

for i in range(1,11):
    lista.append(random.randit(1,10))
print(lista)

for numero in lista:
    cuadrados.append(numero**2)
    cubos.append(numero**3)

print(cuadrados)
print(cubos)