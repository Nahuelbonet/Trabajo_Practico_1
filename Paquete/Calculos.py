# Ejercicio 8:
# Genere un segundo módulo en el cual existan las funciones necesarias para la gestión del
# equipo de recursos humanos de la empresa.
# En el mismo debe existir una primera función que calcule el valor del salario de cada
# empleado. El valor del mismo es la cantidad de horas trabajadas multiplicadas por 10 y un
# incremento del 3% por cada año de antigüedad.
# También debe haber una segunda función que calcule la productividad del empleado. La
# misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de
# horas de trabajo.
# En tercer lugar debe haber una función que reporte toda la información del empleado
# incluyendo la calculada en las dos funciones anteriores, nombre y edad.



def calcular_salario(horas_trabajadas, anos_antiguedad):

    salario_base = horas_trabajadas * 10
    incremento = salario_base * (0.03 * anos_antiguedad)
    salario_total = salario_base + incremento
    
    return salario_total

def calcular_productividad(artefactos_producidos, horas_trabajadas):

    if horas_trabajadas == 0:
        return 0 
    productividad = artefactos_producidos / horas_trabajadas
    
    return productividad