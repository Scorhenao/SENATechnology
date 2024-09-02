# Inicializar lista para almacenar los datos
lista = []

# Solicitar los datos para tres empleados
for i in range(3):
    print("\n--------Bienvenido--------")
    NOMBRE = input("Ingrese su nombre: ")
    VR_HORA = float(input("Ingrese sus ingresos por hora: "))
    HT = int(input("Ingrese sus horas trabajadas: "))
    HED = int(input("Ingrese sus horas diurnas trabajadas: "))
    HEN = int(input("Ingrese sus horas nocturnas trabajadas: "))
    
    VR_HN = VR_HORA * HT
    VR_HED = VR_HORA * HED * 1.25
    VR_HEN = VR_HORA * HEN * 1.35
    
    TOTAL_GANADO = VR_HN + VR_HED + VR_HEN
    
    SALUD = 12
    PENSION = 16
    RIESGO = 1
    
    deducción_salud = TOTAL_GANADO * (SALUD / 100)
    deducción_pensión = TOTAL_GANADO * (PENSION / 100)
    deducción_riesgo = TOTAL_GANADO * (RIESGO / 100)
    
    TOTAL_GANADO_MENOS_DEDUCCIONES = TOTAL_GANADO - deducción_salud - deducción_pensión - deducción_riesgo
    
    lista.append([NOMBRE, VR_HORA, HT, HED, HEN, VR_HN, VR_HED, VR_HEN, TOTAL_GANADO, TOTAL_GANADO_MENOS_DEDUCCIONES])
    
    print(f"\n{NOMBRE} su valor según sus horas normales trabajadas es: {VR_HN}")
    print(f"{NOMBRE} su valor según sus horas extras diurnas es: {VR_HED}")
    print(f"{NOMBRE} su valor según sus horas extras nocturnas es: {VR_HEN}")
    print(f"{NOMBRE} su total ganado es: {TOTAL_GANADO}")
    print(f"\nEl total menos deducción de salud ({SALUD}%): {TOTAL_GANADO - deducción_salud}")
    print(f"El total menos deducción de pensión ({PENSION}%): {TOTAL_GANADO - deducción_salud - deducción_pensión}")
    print(f"El total menos deducción de riesgo ({RIESGO}%): {TOTAL_GANADO_MENOS_DEDUCCIONES}")
    print(f"{NOMBRE} su devengado es: {TOTAL_GANADO_MENOS_DEDUCCIONES}")


# Mostrar la lista final con todos los resultados organizado
print("\n-------Lista de resultados-------")
print(lista)
