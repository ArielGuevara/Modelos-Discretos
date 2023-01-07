def initializateTriangule():
    """La funcion permite generar el triangulo

    Returns:
        float: largo del triangulo
        float: ancho del triangulo
    """
    #ciclo de validacion para el ingreso del lado largo del triangulo
    while True:
        try:
            base = float(input("Ingrese la base del triangulo: "))
            if base > 0:
                break
            else:
                print("Debe ser numero mayor a cero")
        except:
            print("Debe ingresar solo numeros")

    #ciclo de validacion para el ingreso de la altura triangulo
    while True:
        try:
            height = float(input("Ingrese el lado ancho del triangulo: "))
            if height > 0:
                break
            else:
                print("Debe ser numero mayor a cero")
        except:
            print("Debe ingresar solo numeros") 

    return base, height


def calculateArea(base:float, height:float)->float:
    """calcula el area del triangulo

    Args:
        base (float): la base del triangulo
        height (float): altra del traingulo

    Returns:
        float: el area del triangulo
    """
    area = (base * height)/2

    return area

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    base = 0
    height = 0
    area = 0
    print("\tBienvenido al sistema para calcular el area de un triangulo rectangulo")
    print("1._ Debe ingresar la base del triangulo")
    print("2._ Debe ingresar la altura del trinagulo\n")
    (base, height) = initializateTriangule()
    
    area = calculateArea(base, height)
    print("El area del triangulo es: " + str(area))

#**************************************
#  Aqui termina la funcion principal  *
#**************************************