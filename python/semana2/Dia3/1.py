# Preguntar 6 personas el sexo, la edad, el billete que gana. Numero de hombres y mujeres. Salario de ambos. Promedio de edad de hombre y mujeres

CH = 0 #Contador de hombres
CM = 0 #Contador de mujeres
AEH = 0 #Acumulado de edad de hombres
AEM = 0 #Acumulado de edad de mujeres
ASH = 0 #Acumulado salario hombres
ASM = 0 #Acumulado salario mujeres
    
for i in range(6):
    sexo = input("digite su sexo H es para hombres F para mujeres: ").upper()
    edad = int(input("digite su edad: "))
    salario = float(input("digite su salario: "))

    if sexo == "H":
        CH = CH + 1
        ASH = ASH + salario
        AEH = AEH + edad

    elif sexo == "F":
        CM = CM + 1
        ASM = ASM + salario
        AEM = AEM + edad

    else:
        print("Sexo no valido")
        
PEH = AEH / CH #Promedio de edad de hombres
PEM = AEM / CM #Promedio de edad de mujeres
print(f"La cantidad de hombres es: {CH}\n" + 
        f"La cantidad de mujeres es: {CM}\n" + 
            f"El acumulado de salario de los hombre es: {ASH}\n" +
                f"El acumulado de salario de las muejres es: {ASM}\n" +
                f"El promedio de edad de los hombres es: {PEH}\n" + 
                f"El promedio de edad de las mujeres es: {PEM}\n")