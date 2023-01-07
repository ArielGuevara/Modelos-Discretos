def enterVariables():
    """la funcion permite calcular la expresion answer = x^y

    Returns:
        int: retorna el resultado de la expresion
    """
    while True:
        try:
            x = float(input("Ingrese el valor de la base 'x': "))
            break
        except:
            print("Debe ingresar solo numeros")

    while True:
        try:
            print("\t\tEl exponente no debe ser mayo a 100 o menor a -100")
            y = float(input("Ingrese el exponente 'y': "))
            if y > -100 and y < 100:
                break
            else:
                print("El valor ingresado sobrepasa el rango preestablecido")
        except:
            print("Debe ingresar solo numeros")

    return x,y

def calculateExpresion(x:float, y:float)->float:
    """calcula la expresion planteada

    Args:
        x (float): base de la potencia
        y (float): exponente de la potencia

    Returns:
        float: resultado de la potencia
    """
    answer = (x**y)
    return answer

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    x = 0
    y = 0
    answer = 0 
    print("\tBienvenido al sistema para calcular la potencia de la forma: x^y")
    print("1._ Debe ingresar la base en este caso 'x'")
    print("2._ Debe ingresar el exponente 'y' al que se va a elevar la ecuacion\n")
    (x, y) = enterVariables()
    answer = calculateExpresion(x,y)

    print("El resultado de la expresion es: " + str(answer))

#**************************************
#  Aqui termina la funcion principal  *
#**************************************