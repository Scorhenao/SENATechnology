#Genera 2 variables y realiza una division validando
div = float(input("Entre el dividendo: "))
divis = float(input("En el divisor: "))
if divis == 0:
    print("No se puede dividir")
else: 
    division = div / divis
    print(f"El resultado es: {division}")