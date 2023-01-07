#importamos la libreria math 
import math

def enterRadius()->float:
    """valida el ingreso del radio

    Returns:
        float: el radio validado
    """
    while True:
        try:
            radius = float(input("Ingrese el radio de la esfera: "))
            if radius > 0:
                break
            else:
                print("El radio debe ser mayor a cero")
        except:
            print("Debe ingresar solo numeros")

    return radius

def calculateVolume(radius:float)->float:
    """calcula el volumen de una esfera

    Args:
        radius (float): el radio de la esfera

    Returns:
        float: el volumen de la esfera
    """
    volume = 4*(math.pi*radius**3)/3

    return volume

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    radius = 0
    volume = 0

    radius = enterRadius()

    volume = calculateVolume(radius)
    
    print(f"el valor del volumen de la esfera es de: {volume}")

#**************************************
#  Aqui termina la funcion principal  *
#**************************************