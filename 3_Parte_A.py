# 3 - Especializar la función del punto 1 para que valide el número en un rango determinado
# pasado por parámetro “desde”-“hasta”.

def mostrar_numero_en_rango(numero, desde, hasta):
    if desde <= numero <= hasta:
        print("El número", numero, "está dentro del rango.")
    else:
        print("El número", numero, "no está dentro del rango.")

mostrar_numero_en_rango(5, 1, 100)
mostrar_numero_en_rango(15, 1, 10) 