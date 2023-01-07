#importacion de la libreria os
import os

def celciusToFahrenheit()->float:
    """convierte de celcius a fahrenheit

    Returns:
        float: grados Fahrenheit
    """
    while True:
        try:
            celcius = float(input("Ingrese los grados en celcius: "))
            break
        except:
            print("Debe ingresar solo numeros")

    fahrenheit = ((celcius*9)/5 + 23)
    print("Los " + str(celcius) + " grados Celcius ", end = "")
    return fahrenheit

def fahrenheitToCelcius()->float:
    """transforma de Fahrenheit a Celcius

    Returns:
        float: grados Celcius
    """
    while True:
        try:
            fahrenheit = float(input("Ingrese los grados en celcius: "))
            break
        except:
            print("Debe ingresar solo numeros")

    celcius = ((fahrenheit-32)*5/9)

    print("Los " + str(fahrenheit) + " grados Fahrenheit ", end = "")
    return celcius

def validateOption()->int:
    """la funcion valida que la variable opcion sea numerica

    Returns:
        int: opcion
    """
    while True:
        try:
            opt = int(input(">: "))
            break
        except:
            print("Debe ingresar solo numeros")
    return opt

def menu():
    """devuelve el menu disponible
    """
    print("*********************************")
    print("*\t\tMENU\t\t*")
    print("*********************************")
    print("[1] -> Transformar de grados Celcius a Fahrenheit")
    print("[2] -> Transformar de grados Fahrenheit a Celcius")
    print("[3] -> Salir")
#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    option = 0
    while True:
        #limpieza de pantalla
        os.system("cls")
        print("\tBienvenido al sistema para hacer la conversion de Celcius a Fahrenheit y viceversa")
        #llamada a menu
        menu()
        print("\tIngrese una opcion")
        option = validateOption()
        match option:
            case 1:
                print("equivalen a " + str(celciusToFahrenheit()) + " Fahrenheit")
                os.system("pause")
            case 2:
                print("equivalen a " + str(fahrenheitToCelcius()) + " Celcius")
                os.system("pause")
            case 3:
                print("\t\tGracias por usar el programa")
                break
            case _:
                print("opcion no valida")
                
#**************************************
#  Aqui termina la funcion principal  *
#**************************************