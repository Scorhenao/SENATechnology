# cree una lista con la cc de un paciente, el nombre, el salario por hora, horas trabajadas, numero de horas diestras diurnas

#[cc,nombre,sh,ht,nhed]

# luego va a calcular el salario de cada trabajador y lo mete en una lista aparte

# si trabaja 1 hora extra se le da un 35% de recargo 


pacientes = []

for i in range(1):
    cc = int(input("cc: "))
    nombre = input("nombre: ")
    sh = int(input("salario por hora: "))
    ht = int(input("horas trabajadas: "))
    nhed = int(input("numero de horas extras diurnas: "))
    thed = (nhed * sh) * 1.35 #total de horas extras diurnas mas el 35%
    t = sh * ht + thed #total a pagar mas horas diurnas extras
    pacientes.append([cc, nombre, sh, ht, nhed, thed, t])
    

print(pacientes)



