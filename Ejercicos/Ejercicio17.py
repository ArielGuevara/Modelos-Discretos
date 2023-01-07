def validateNumbers()->float:
    """valida el ingreso de los numeros a operarse

    Returns:
        float: numero validado
    """
    while True:
        try:
            number = float(input("Ingrese el numero: "))
            break
        except:
            print("Debe ingresar solo numeros")
    return number

def validateRange()->int:
    """valida el limite de los numeros a operarse

    Returns:
        int: el limite
    """
    while True:
        try:
            number = int(input("Ingrese cuantos numeros desea operar: "))
            break
        except:
            print("Debe ingresar solo numeros")
    return number

def validateExponent()->float:
    """valida que el exponente sea el que esta establecido en el rango

    Returns:
        float: exponente
    """
    while True:
        try:
            print("\t\tEl exponente no debe ser mayo a 100 o menor a -100")
            number = float(input("Ingrese el exponente: "))
            if number > -100 and number < 100:
                break
            else:
                print("El valor ingresado sobrepasa el rango preestablecido")
        except:
            print("Debe ingresar solo numeros")
    return number

def calcualateExpresion(limit:int, exponent:float)->float:
    """calcula la expresion en funcion de los parametros 

    Args:
        limit (int): limite de los numeros a operarse
        exponent (float): numero al que se van a elevar todos los numeros

    Returns:
        float: resultado de toda esa expresion
    """
    values = []
    result = 0
    for i in range(0,limit):
        values.append(validateNumbers())

    for number in values:
        result += (number**exponent)

    return result


    #*********************************
    #  Esta es la función principal  *
    #*********************************
    if __name__ == "__main__":
        #inicializacion de variables
        exponent = 0
        limit = 0
        result = 0
        print("\tBienvenido al sistema para calcular la expresion de la forma ")
        print("\t\tresultado = a^n + b^n + c^n + ... + z^n+y^n")
        print("1._ Debe ingresar la cantidad de numeros a operarse")
        print("2._ Debe ingresar el exponente con el cual se van a potenciar todos los numeros")
        limit = validateRange()
        exponent = validateExponent()

        result = calcualateExpresion(limit, exponent)

        print(f"El resultado se de la expresion es: {result}")

    #**************************************
    #  Aqui termina la funcion principal  *
    #**************************************