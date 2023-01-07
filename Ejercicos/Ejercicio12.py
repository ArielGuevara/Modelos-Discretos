def enterVariables():
    """valida el ingreso para time y distance 

    Returns:
        float: las variables time y distance
    """
    while True:
        try:
            distance = float(input("Ingrese la distancia en metros: "))
            if distance > 0:
                break
            else:
                print("Vamos a regirnos solo en lo que avanzas no en lo que regresas")
        except:
            print("Debe ingresar solo numeros")

    while True:
        try:
            time = float(input("Ingrese el tiempo en segundos: "))
            if time > 0:
                break
            else:
                print("Aun no podemos regresar en el tiempo :v ")
        except:
            print("Debe ingresar solo numeros")

    return time, distance

def calculateVelocity(time:float, distance:float)->float:
    """calcula la velociad en funcion del tiempo y la distancia

    Args:
        time (float): tiempo empleado en recorrer una distancia
        distance (float): longitud recorrida

    Returns:
        float: velocidad
    """
    velocity = distance/time

    return velocity

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    time = 0
    velocity = 0
    distance = 0    

    (time, distance) = enterVariables()
    velocity = calculateVelocity(time,distance)
    print("El valor de la velociad es de: " + str(velocity) + " metros por segundo")

#**************************************
#  Aqui termina la funcion principal  *
#**************************************