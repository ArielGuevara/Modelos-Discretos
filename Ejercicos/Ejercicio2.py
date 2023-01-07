def initializateRectangule():
    """La funcion permite generar el rectangulo

    Args:
        length (float): lado largo del rectangulo
        width (float): lado ancho del rectangulo

    Returns:
        float: largo del rectangulo
        float: ancho del rectangulo
    """
    #ciclo de validacion para el ingreso del lado largo del rectangulo
    while True:
        try:
            length = float(input("Ingrese el lado largo del rectangulo: "))
            if length > 0:
                break
            else:
                print("Debe ser numero mayor a cero")
        except:
            print("Debe ingresar solo numeros")

    #ciclo de validacion para el ingreso del lado ancho del rectangulo
    while True:
        try:
            width = float(input("Ingrese el lado ancho del rectangulo: "))
            if length > width:
                break
            else:
                print("El lado ancho debe ser mas corto que el lado largo")
        except:
            print("Debe ingresar solo numeros") 

    return length, width

def calculatePerimeter(length:float, width:float)->float:
    """la funcion calcula el perimetro del rectangulo

    Args:
        length (float): lado largo del rectangulo
        width (float): lado ancho del rectangulo

    Returns:
        float: perimetro del rectangulo
    """
    result = (length*2) + (width*2)
    return result

def calculateArea(length:float, width:float)->float:
    """la funcion calcula el area del rectangulo

    Args:
        length (int): lado largo del rectangulo
        width (int): lado ancho del rectangulo

    Returns:
        float: area del rectangulo
    """
    result = length * width
    return result

def instruccions():
    """devuelve las intrucciones del programa
    """
    print("*" * 80)
    print("* Bienvenido al programa para calcular el area y perimetro de un rectangulo *")
    print("1._ Debe ingresar el lado largo del rectangulo")
    print("2._ Debe ingresar el lado ancho del rectangulo")
    print("*" * 80)

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    length = 0
    width = 0
    area = 0
    perimeter = 0
    #llamamos a las instrucciones
    instruccions()
    #generamos el rectangulo
    (length, width) = initializateRectangule()
    #calculamos el perimetro
    perimeter = calculatePerimeter(length,width)
    #mostramos por pantalla el valor del perimetro
    print("El perimetro del rectangulo es de: " + str(perimeter))
    #calculculamos el area del rectangulo
    area = calculateArea(length, width)
    #mostramos por pantalla el valor del area
    print("El area del rectangulo es de: " + str(area))
#**************************************
#  Aqui termina la funcion principal  *
#**************************************
