# Sumar todas las filas y columnas, suma de diagonal principal, suma de la diagonal secundaria y suma de la fila central en una matriz
matriz =[
        [3,8,5,4,2], # 22
        [6,9,4,3,7], # 29
        [8,12,6,4,3], # 33 
        [9,6,8,2,10], # 35
        [5,8,7,9,6] # 35
        #31 43 30 22 28
        # 3 9 6 2 6 diagonal principal
        # 2 3 6 6 5 diagonal secundaria
        ]

SF = 0 # Suma de filas
SC = 0 # Suma de columnas
SDP = 0 # Suma de diagonal principal
SDS = 0 # Suma de diagonal secundaria

for i in range(len(matriz)):
    # suma las filas 
    SF = SF + sum(matriz[i])
    # suma de la diagonal principal
    SDP = SDP + matriz[i][i]
    # suma de la diagonal secundaria
    SDS = SDS + matriz[i][len(matriz) - 1 - i]
    for j in range(len(matriz)):
        # suma de columnas
        SC = SC + matriz[i][j]
        
# suma de la diagonal secundaria

# imprimir resultados
print(f"""
Suma de filas: {SF}
Suma de columnas: {SC}
Suma de diagonal principal: {SDP}
Suma de diagonal secundaria: {SDS}""")

print("\n matriz: ")
# mostrar matriz con espacio para que se entienda
for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end=" ")
    print()
