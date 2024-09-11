# 5 - Realizar un programa que: asigne a la variable numero1 un valor solicitado al usuario,
# valide el mismo entre 10 y 100, realice un descuento del 5% a dicho valor a través de una
# función llamada realizarDescuento(). Mostrar el resultado por pantalla. Atención: pueden
# reutilizarse funciones ya creadas.


def realizar_descuento(valor):
    return valor * 0.95

numero1 = int(input("Ingresa un valor entre 10 y 100: "))


while numero1 < 10 or numero1 > 100:
    print("El valor ingresado no es válido. Debe estar entre 10 y 100.")
    numero1 = int(input("Ingresa un valor entre 10 y 100: "))

resultado = realizar_descuento(numero1)

print(f"El valor con el descuento es: {resultado}")