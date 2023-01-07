#importamos la libreria math
import math 

def calculateArea()->float:
    """la funcion calcula el area de un circulo

    Returns:
        float: el area del circulo
    """
    while True:
        try:
            radius = float(input("Ingrese el radio del circulo: "))
            if radius > 0:
                break
            else:
                print("El radio debe ser mayor a cero")
        except:
            print("Debe ingresar solo numeros")

    #usamos la libreria math para usar pi 
    area = math.pi * (radius ** 2)

    return area

def instruccions():
    """devuelve las intrucciones del programa
    """
    print("*" * 80)
    print("* Bienvenido al programa para calcular el area de un circulo")
    print("1._ Debe ingresar el radio del circulo y se devolvera el area")
    print("*" * 80)

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":

    #llamada a las instrucciones
    instruccions()
    #llamada a la funcion 
    print("El area del circulo es de: " + str(calculateArea()))
#**************************************
#  Aqui termina la funcion principal  *
#**************************************