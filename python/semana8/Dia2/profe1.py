departamentos = ["contabilidad", "Administración", "contabilidad", "Administración", "contabilidad"]
empleados = ["Juan Pérez", "Ana Gómez", "Luis Martínez", "Carlos Ruiz", "Marta Sánchez"]
salarios = [3000, 2500, 3200, 2800, 3100]

# Ordenar los datos por departamento
n = len(departamentos)
for i in range(n-1):
    for j in range(n-1-i):
        if departamentos[j].lower() > departamentos[j+1].lower():  # Comparar en minúsculas para evitar problemas con mayúsculas
            # Intercambiar departamentos
            departamentos[j], departamentos[j+1] = departamentos[j+1], departamentos[j]
            # Intercambiar empleados
            empleados[j], empleados[j+1] = empleados[j+1], empleados[j]
            # Intercambiar salarios
            salarios[j], salarios[j+1] = salarios[j+1], salarios[j]

# Inicializar variables
total_departamento = 0
departamento_actual = departamentos[0]

print("Total de salarios por departamento:")

# Utilizar un while para realizar el rompimiento de control
i = 0
while i < len(departamentos):
    if departamentos[i] == departamento_actual:
        total_departamento += salarios[i]
    else:
        print(f"{departamento_actual}: {total_departamento}")
        departamento_actual = departamentos[i]
        total_departamento = salarios[i]
    i += 1

# Imprimir el último departamento
print(f"{departamento_actual}: {total_departamento}")

# Mostrar las listas ordenadas (opcional)
print("\nDepartamentos ordenados:", departamentos)
print("Empleados ordenados:", empleados)
print("Salarios ordenados:", salarios)
