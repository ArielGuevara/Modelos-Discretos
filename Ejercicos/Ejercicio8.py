#importamos la libreria math y os
import math, os

def enterRadius()->float:
    while True:
        try:
            radius = float(input("Ingrese el radio del circulo: "))
            if radius > 0:
                break
            else:
                print("El radio debe ser mayor a cero")
        except:
            print("Debe ingresar solo numeros")
    return radius

def calculateArea(radius:float)->float:
    """la funcion calcula el area de un circulo

    Args:
        radius (float): radio del circulo

    Returns:
        float: el area del circulo
    """
    #usamos la libreria math para usar pi 
    area = math.pi * (radius ** 2)

    return area

def calculateDiameter(radius:float)->float:
    """la funcion devuelve el diametro de un circulo

    Args:
        radius (float): radio del circulo

    Returns:
        float: diametro del circulo
    """
    diameter = (radius*2)
    return diameter

def calculatePerimeter(radius:float)->float:
    """la funcion devuelve el perimetro de un circulo

    Args:
        radius (float): radio del circulo

    Returns:
        float: perimetro del circulo
    """
    perimeter = (2*math.pi*radius)

    return perimeter

def validateOption()->int:
    """la funcion valida que la variable opcion sea numerica

    Returns:
        int: opcion
    """
    while True:
        try:
            opt = int(input(">: "))
            break
        except:
            print("Debe ingresar solo numeros")
    return opt


def menu():
    """devuelve el menu disponible
    """
    print("*********************************")
    print("*\t\tMENU\t\t*")
    print("*********************************")
    print("[1] -> Ingresar el valor del radio")
    print("[2] -> Calcular el area del cirulo")
    print("[3] -> Calcular el perimetro del cirulo")
    print("[4] -> Calcular el diametro del cirulo")
    print("[5] -> Salir")

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":

    #incializacion de variables
    radius = 0
    perimeter = 0
    area = 0
    diameter = 0
    option = 0
    #ciclo del menu
    while True:
        #limpieza de pantalla
        os.system("cls")
        print("\tBienvenido al sistema para calcular atributos de un circulo")
        #llamada a menu
        menu()
        print("\tIngrese una opcion")
        option = validateOption()
        match option:
            case 1:
                #calculo del radio
                radius = enterRadius()
                print("ingreso correcto")
                #pausa para visualizar las respuestas
                os.system("pause")
            case 2:
                #calculo del area
                area = calculateArea(radius)
                print("El area es: " + str(area))
                #pausa para visualizar las respuestas
                os.system("pause")
            case 3:
                #calculo del perimetro
                perimeter = calculatePerimeter(radius)
                print("El perimetro es: " + str(perimeter))
                os.system("pause")
            case 4:
                #calculo del diametro
                diameter = calculateDiameter(radius)
                print("El diametro es: " + str(diameter))
                #pausa para visualizar las respuestas
                os.system("pause")
            case 5:
                #salida
                print("\t\tGracias por usar el programa")
                break
            case _:
                #caso erroneo
                print("opcion no valida")
#**************************************
#  Aqui termina la funcion principal  *
#**************************************