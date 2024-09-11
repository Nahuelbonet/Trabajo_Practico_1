# 4 - Realizar un programa en donde se puedan utilizar los prototipos de la función Restar en
# sus 4 combinaciones.
# restar1(int, int)->int:
# restar2()->int:
# restar3(int, int):
# restar4():


def restar1(a, b) -> int:
    return a - b

def restar2() -> int:
    a = 10
    b = 5
    return a - b

def restar3(a, b):
    resultado = a - b
    print("El resultado de restar3 es:", resultado)

def restar4():
    a = 20
    b = 7
    resultado = a - b
    print("El resultado de restar4 es:", resultado)


print("Resultado de restar1:", restar1(8, 3))
print("Resultado de restar2:", restar2())
restar3(15, 10)
restar4()         