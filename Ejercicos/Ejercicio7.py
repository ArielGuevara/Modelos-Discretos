def calculateExpression()->int:
    """la funcion permite calcular la expresion y = (x^z)/2.5

    Returns:
        int: retorna el resultado de la expresion
    """
    while True:
        try:
            a = float(input("Ingrese el valor de 'a': "))
            break
        except:
            print("Debe ingresar solo numeros")

    while True:
        try:
            print("\t\tEl exponente no debe ser mayo a 100 o menor a -100")
            b = float(input("Ingrese el valor de 'b': "))
            break
        except:
            print("Debe ingresar solo numeros")

    answer = (a + (b**2))/2.5

    return answer

def instruccions():
    """devuelve las intrucciones del programa
    """
    print("*" * 80)
    print("*\tBienvenido al programa para calcular la expresion de la forma: \t*")
    print("\t\tr = (a + b^2)/2.5")
    print("1._ Debe ingresar el valor de 'a'")
    print("2._ Debe ingresar el valor de 'b'")
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
    print("el resutado para la expresion: " + str(answer))

#**************************************
#  Aqui termina la funcion principal  *
#**************************************