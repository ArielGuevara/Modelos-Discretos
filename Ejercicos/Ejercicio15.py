#importamos la libreria math 
import math

def enterNumber()->float:
    """valida el ingreso del numero sea positivo

    Returns:
        float: numero validado
    """
    while True:
        try:
            number = float(input("Ingrese el numero para obtener su raiz: "))
            if number > 0:
                break
            else:
                print("Con un numero negativo obtienes una raiz imaginaria")
        except:
            print("Debe ingresar solo numeros")

    return number

def calculateSquareRoot(number:float)->float:
    """calcula la raiz cuadrada del numero pasado por parametro

    Args:
        number (float): numero al que se le va a sacar la raiz

    Returns:
        float: la raiz del numero
    """
    result = math.sqrt(number)

    return result

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    number = 0
    answer = 0

    number = enterNumber()

    answer = calculateSquareRoot(number)

    print("La raiz cuadrada de " + str(number) + " es: " + str(answer))

#**************************************
#  Aqui termina la funcion principal  *
#**************************************