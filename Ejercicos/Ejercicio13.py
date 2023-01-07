def enterAngles():
    while True:
        try:
            angleA = float(input("Ingrese el angulo A: "))
            if angleA > 0 and angleA <= 178:
                break
            else:
                print("El angulo debe ser mayor a cero y no debe sobrepasar los 178°\n"+
                "para poder dejar un grado de distancia para los dos angulos siguientes")
        except:
            print("Debe ingresar solo numeros")

    while True:
        try:
            angleB = float(input("Ingrese el angulo B: "))
            if angleB > 0 and (angleA + angleB) < 180:
                break
            else:
                print("El angulo debe ser mayor a cero y sumado al angulo B no debe sobrpasar los 180°\n")
        except:
            print("Debe ingresar solo numeros")

    return angleA, angleB

def calculateAngleC(angleA:float, angleB:float)->float:
    """calcula el angulo faltante del triangulo

    Args:
        angleA (float): angulo A
        angleB (float): angulo B

    Returns:
        float: angulo C
    """
    angleC = 180 - (angleA + angleB)

    return angleC

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    angleA = 0
    angleB = 0
    angleC = 0 
    print("\tBienvenido al sistema para encontrar el angulo C de un triangulo")
    print("△ el tringulo esta formado por 3 angulos internos que su suma por regla general "+
    "deben dar 180 grados")
    print("formula △ = αA + αB + αC = 180")
    print("para lo que usted debera ingresar 2 angulos y el programa le devolvera el valor del tercer angulo")

    (angleA, angleB) = enterAngles()
    angleC = calculateAngleC(angleA, angleB)
    print("El valor del ultimo angulo es de: " + str(angleC) + " grados")

#**************************************
#  Aqui termina la funcion principal  *
#**************************************