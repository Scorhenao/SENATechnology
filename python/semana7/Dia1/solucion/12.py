# 12. dada una lista, generar nueva lista ordenada de mayor a menor y eliminar cada uno de los numeros de los numeros resultantes de la lista original

lista = [18,2,32,4,53,6,75,8,9,]

#ordenar liste de mayor a menor
lista_ordenada = sorted(lista, reverse=True)
print(lista_ordenada)
#eliminar los elementos de la lista original
lista.clear()
print(lista)