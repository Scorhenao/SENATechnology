# 1. Lista del 0 al 30 de dos en dos 
# 2.agregar los numero impares y que quede en orden
# 3. programa que tenga una lista de ususuarios con nombre y contraseñas y verificar que el usuario ingresado y la contraseña coincidan con los que hay en dicha lista un (login)
lista = []

# 1
print("------primer punto------")
for i in range(31):
    if i % 2 == 0:
        lista.append(i)
print(f"La lista agregando numeros pares es: {lista}")

# 2
print("------segundo punto------")
index = 0
for i in lista:
    index += 1
    if index == 30:
        break
    if i % 2 == 0:
        lista.insert(index,i+1)
print(f"La lista agregando numeros impares es: {lista}")

# 3
usuarios = [
    ["pepe","123"],
    ["juan","456"],
    ["sam", "789"]
    ]
print("------tercer punto------")
for i in usuarios:
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    # verificar que el usuario y la contraseña esten en la lista usuarios
    if usuario in [user[0] for user in usuarios]:
        if contrasena in [user[1] for user in usuarios]:
            print("login correcto")
            break
    else:
        print("contrasena incorrecta")
        
