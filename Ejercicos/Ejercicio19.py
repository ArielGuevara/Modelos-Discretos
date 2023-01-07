#importamos la libreria math 
import math

def enterVariables():
    """la funcion valida el ingreso de las variable a,b,c 

    Returns:
        int: retorna el resultado de la expresion
    """
    while True:
        try:
            b = float(input("Ingrese el valor de 'b': "))
            break
        except:
            print("Debe ingresar solo numeros")

    while True:
        try:
            c = float(input("Ingrese el valor de 'c': "))
            break
        except:
            print("Debe ingresar solo numeros")

    while True:
        try:
            a = float(input("Ingrese el valor de 'a': "))
            break
        except:
            print("Debe ingresar solo numeros")

    return a,b,c

def calculateExpression(a:float,b:float,c:float):
    """calcula la expresion

    Args:
        a (float): valor de a
        b (float): valor de b
        c (float): valor de c
    """
    if (b**2 + c) < 0:
        imaginaria =  (b**2+c) * (-1)
        print(f"{-b/2*a} + {imaginaria}i/{2*a}")
    else: 
        result = (-b+math.sqrt((b**2)+c))/2*a
        print(f"El resultado de la expresion es: {result}")

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    a = 0
    b = 0
    c = 0

    a,b,c = enterVariables()

    calculateExpression(a,b,c)

#**************************************
#  Aqui termina la funcion principal  *
#**************************************