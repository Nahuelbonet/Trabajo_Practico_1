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

    
from reportes import reporte_empleado


nombre = "Juan"
edad = 30
horas_trabajadas = 160
anos_antiguedad = 5
artefactos_producidos = 50


print(reporte_empleado(nombre, edad, horas_trabajadas, anos_antiguedad, artefactos_producidos))