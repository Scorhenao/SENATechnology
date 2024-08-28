# 11. capacidad anual de gastos por estrato
# cuanto dinero en cada prenda y cuanto dinero en total
# trabaje con cuatro prendas

prendas =[
    "pantalones",
    "camisas",
    "zapatos",
    "interiores"
]

capacidadPorAñoEstrato1 = 0
capacidadPorAñoEstrato2 = 0
capacidadPorAñoEstrato3 = 0
capacidadPorAñoEstrato4 = 0
capacidadPorAñoEstrato5 = 0


for i in range(4):
    estrato = int(input("\nIgrese su estrato: "))
    
    if estrato < 1 or 4:
        print("No existe ese estrato")
        exit()
        
    print("""
        1. pantalones
        2. camisas
        3. zapatos
        4. interiores
        """)
    
    prenda = int(input("Ingrese la prenda: "))

    if prenda != 1 and 2 and 3 and 4:
        print("Esta prenda no existe!")
        exit()

    match prenda:
        case 1:
            precioDePrenda = float(input(f"Ingrese el precio gastado en la prenda {prendas[0]}: "))
            capacidadPorAñoEstrato1 += precioDePrenda
        case 2:
            precioDePrenda = float(input(f"Ingrese el precio gastado en la prenda {prendas[1]}: "))
            capacidadPorAñoEstrato2 += precioDePrenda
        case 3:
            precioDePrenda = float(input(f"Ingrese el precio gastado en la prenda {prendas[2]}: "))
            capacidadPorAñoEstrato3 +=precioDePrenda
        case 4:
            precioDePrenda = float(input(f"Ingrese el precio gastado en la prenda {prendas[3]}: "))
            capacidadPorAñoEstrato4 +=precioDePrenda
        case _:
            print("No existe esa prenda")
            continue
        
print(f"""
    El total gastado por el estrato 1 es: {capacidadPorAñoEstrato1}
    El total gastado por el estrato 2 es: {capacidadPorAñoEstrato2}
    El total gastado por el estrato 3 es: {capacidadPorAñoEstrato3}
    El total gastado por el estrato 4 es: {capacidadPorAñoEstrato4}
    """)