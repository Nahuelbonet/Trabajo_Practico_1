# 6 - Realizar un programa que: asigne a las variables numero1 y numero2 los valores
# solicitados al usuario, valide los mismos entre 10 y 100, asigne a la variable operacion el
# valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice la operación de dichos valores
# a través de una función. Mostrar el resultado por pantalla

def realizarOperacion(num1, num2, operacion):
    if operacion == 's':
        return num1 + num2
    elif operacion == 'r':
        return num1 - num2
    else:
        return None

numero1 = int(input("Ingresa un valor entre 10 y 100: "))
while numero1 < 10 or numero1 > 100:
    print("El valor ingresado no es válido. Debe estar entre 10 y 100.")
    numero1 = int(input("Ingresa el primer valor entre 10 y 100: "))

numero2 = int(input("Ingresa el segundo valor entre 10 y 100: "))
while numero2 < 10 or numero2 > 100:
    print("El valor ingresado no es válido. Debe estar entre 10 y 100.")
    numero2 = int(input("Ingresa el primer valor entre 10 y 100:"))

operacion = input("Ingresa la operación ('s' para sumar, 'r' para restar): ").lower()
while operacion not in ['s', 'r']:
    print("Operación no válida. Tenes que ingresar 's' para sumar o 'r' para restar.")
    operacion = input("Ingresa la operación ('s' para sumar, 'r' para restar): ").lower()

resultado = realizarOperacion(numero1, numero2, operacion)

if resultado is not None:
    if operacion == 's':
        print(f"La suma de {numero1} y {numero2} es: {resultado}")
    elif operacion == 'r':
        print(f"La resta de {numero1} y {numero2} es: {resultado}")
else:
    print("Operación no válida.")