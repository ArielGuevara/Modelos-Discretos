#importacion de la libreria math
import math
def enterLegs():
    """la funcion valida el ingreso de los catetos

    Returns:
        float: los dos catetos 
    """
    while True:
        try:
            #ingreso del cateto A
            legA = float(input("Ingrese el cateto 'a': "))
            break
        except:
            print("Debe ingresar solo numeros")
    
    while True:
        try:
            #ingreso del cateto B
            legB = float(input("Ingrese el cateto 'b': "))
            break
        except:
            print("Debe ingresar solo numeros")

    return legA, legB

def calculatePithagorasTheorem(legA:float, legB:float)->float:
    """la funcion calcula la hipotenusa

    Args:
        legA (float): cateto A
        legB (float): cateto B

    Returns:
        float: Hipotenusa
    """
    hypotenuse = math.sqrt((legA**2)+(legB**2))
    return hypotenuse

def instruccions():
    """devuelve las intrucciones del programa
    """
    print("*" * 80)
    print("* Bienvenido al programa para calcular el teorema de Pitagoras")
    print("\t\t C = raizCuadrada(A^2 + B^2)")
    print("1._ Debe ingresar el cateto A")
    print("2._ Debe ingresar el cateto B")
    print("*" * 80)

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    hypotenuse = 0
    legA = 0
    legB = 0
    #llamada a las instrucciones
    instruccions()
    #ingreso de los catetos validados
    (legA, legB) = enterLegs()
    #calculo de la hipotenusa
    hypotenuse = calculatePithagorasTheorem(legA, legB)

    print("La hipotenusa vale: " + str(hypotenuse))

#**************************************
#  Aqui termina la funcion principal  *
#**************************************