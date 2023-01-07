def initializateParalelogram():
    """La funcion permite generar el paralelogramo

    Returns:
        float: largo del paralelogramo
        float: ancho del paralelogramo
    """
    #ciclo de validacion para el ingreso del lado largo del paralelogramo
    while True:
        try:
            base = float(input("Ingrese la base del paralelogramo: "))
            if base > 0:
                break
            else:
                print("Debe ser numero mayor a cero")
        except:
            print("Debe ingresar solo numeros")

    #ciclo de validacion para el ingreso de la altura paralelogramo
    while True:
        try:
            height = float(input("Ingrese el lado ancho del paralelogramo: "))
            if height > 0:
                break
            else:
                print("Debe ser numero mayor a cero")
        except:
            print("Debe ingresar solo numeros") 

    return base, height


def calculateArea(base:float, height:float)->float:
    """calcula el area del paralelogramo

    Args:
        base (float): la base del paralelogramo
        height (float): altra del paralelogramo

    Returns:
        float: el area del paralelogramo
    """
    area = (base * height)

    return area

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    base = 0
    height = 0
    area = 0
    print("\tBienvenido al sistema para calcular el area de un paralelogramo")
    print("1._ Debe ingresar la base del paralelogramo")
    print("2._ Debe ingresar la altura del paralelogramo\n")
    (base, height) = initializateParalelogram()
    
    area = calculateArea(base, height)
    print("El area del paralelogramo es: " + str(area))

#**************************************
#  Aqui termina la funcion principal  *
#**************************************