# Ejercicio 9:
# Genere un paquete con ambos módulos.


from Calculos import calcular_salario, calcular_productividad

def reporte_empleado(nombre, edad, horas_trabajadas, anos_antiguedad, artefactos_producidos):
    """
    Genera un reporte completo de un empleado.
    
    :param nombre: Nombre del empleado.
    :param edad: Edad del empleado.
    :param horas_trabajadas: Cantidad de horas trabajadas por el empleado.
    :param anos_antiguedad: Años de antigüedad del empleado.
    :param artefactos_producidos: Cantidad de artefactos producidos por el empleado.
    :return: Reporte con la información del empleado.
    """
    salario = calcular_salario(horas_trabajadas, anos_antiguedad)
    productividad = calcular_productividad(artefactos_producidos, horas_trabajadas)
    
    reporte = f"Nombre: {nombre}\n" \
              f"Edad: {edad}\n" \
              f"Salario: {salario}\n" \
              f"Productividad: {productividad}\n" \
              f"Horas trabajadas: {horas_trabajadas}\n" \
              f"Años de antigüedad: {anos_antiguedad}\n" \
              f"Artefactos producidos: {artefactos_producidos}"
    
    return reporte