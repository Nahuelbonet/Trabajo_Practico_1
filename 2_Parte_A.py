# #2 - Crear una función que permita determinar si un número es par o no. La función retorna
# “True” en caso afirmativo y “False” en caso contrario. Probar en el programa principal
# realizando la invocación o llamada


def numero(par) -> True:
    if (par % 2) == 0 :
        print(f"El numero {par} es par")
        
    else:
        print(f"El numero {par} es impar")
    
numero(6)
numero(3)
numero(7)
numero(8)