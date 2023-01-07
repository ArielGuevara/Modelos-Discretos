def calculateExpression()->int:
    """la funcion permite calcular la expresion y = (x^z)/2

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
            z = float(input("Ingrese el exponente 'z': "))
            if z > -100 and z < 100:
                break
            else:
                print("El valor ingresado sobrepasa el rango preestablecido")
        except:
            print("Debe ingresar solo numeros")

    y = (x**z)/2

    return y

def instruccions():
    """devuelve las intrucciones del programa
    """
    print("*" * 80)
    print("*\tBienvenido al programa para calcular la expresion de la forma: \t*")
    print("\t\ty = (x^z)/2")
    print("1._ Debe ingresar la base en este caso 'x'")
    print("2._ Debe ingresar el exponente 'z' al que se va a elevar la ecuacion")
    print("*" * 80)

#*********************************
#* Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #Inicializacion de la variable
    answer = 0
    #llamada a la funcion de intrucciones
    instruccions()
    #llamada a la funcion
    answer = calculateExpression()
    print("el resutado para 'y': " + str(answer))

#**************************************
#  Aqui termina la funcion principal  *
#**************************************