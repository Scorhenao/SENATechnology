# 13. Recorra la siguiente lista e imprima uno a uno sus elementos
# lista = ["Antioquia", "Medellin", "Bello", "itagui"], ["Cundinamarca", "Bogota", "Chia", "Soacha"],["Valle", "Cali", "Buga", "Jamundi"]

lista = ["Antioquia", "Medellin", "Bello", "itagui"], ["Cundinamarca", "Bogota", "Chia", "Soacha"],["Valle", "Cali", "Buga", "Jamundi"]

#Imprima uno a uno sus elementos enumerados 

for index, sublist in enumerate(lista):
    for item in sublist:
        print(f"{index+1} {item}")
