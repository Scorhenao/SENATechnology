departamentos = ["contabilidad", "Administración", "contabilidad", "Administración", "contabilidad"]
empleados = ["Juan Pérez", "Ana Gómez", "Luis Martínez", "Carlos Ruiz", "Marta Sánchez"]
salarios = [3000, 2500, 3200, 2800, 3100]

# Inicializar los totales de salario por departamento
total_contabilidad = 0
total_administracion = 0

# Calcular los totales de salario por departamento
total_contabilidad = sum(salarios[i] for i in range(len(departamentos)) if departamentos[i].lower() == "contabilidad")
total_administracion = sum(salarios[i] for i in range(len(departamentos)) if departamentos[i].lower() == "administración")


# Mostrar los resultados
print("Total salario en Contabilidad:", total_contabilidad)
print("Total salario en Administración:", total_administracion)
