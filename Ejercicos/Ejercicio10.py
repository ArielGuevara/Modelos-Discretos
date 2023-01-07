#importacion de la libreria os
import os

def enterCentimeters()->float:
    """la funcion valida el ingreso de los centimetros

    Returns:
        float: centimetros
    """
    while True:
        try:
            centimeters = float(input("Ingrese los centimetros: "))
            if centimeters > 0:
                break
            else:
                print("El valor debe ser mayor a cero")
        except:
            print("Debe ingresar solo numeros")

    return centimeters

def convertToMeters(centimeters:float)->float:
    """la funcion convierte los centimetros a metros

    Args:
        centimeters (float): valor de los centimetros

    Returns:
        float: conversion de centimetros a metros
    """
    meters = centimeters / 100

    return meters

def convertToKilometers(centimeters:float)->float:
    """la funcion convierte los centimetros a kiolemtros

    Args:
        centimeters (float): valor de los centimetros

    Returns:
        float: conversion de centimetros a Kilometros
    """
    kilometers = centimeters / 100000

    return  kilometers

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
    print("[1] -> Ingresar el valor en centimetros")
    print("[2] -> Transformar a metros")
    print("[3] -> Transformar a kilometros")
    print("[4] -> Salir")

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    option = int(0)
    centimeters = 0
    meters = 0
    kilometers = 0
    while True:
        #limpieza de pantalla
        os.system("cls")
        print("\tBienvenido al sistema para transformar los centimetros a metros o kilometros")
        #llamada a menu
        menu()
        print("\tIngrese una opcion")
        option = validateOption()
        match option:
            case 1:
                centimeters = enterCentimeters()
                print("ingreso correcto")
                os.system("pause")
            case 2:
                meters = convertToMeters(centimeters)
                print("los " + str(centimeters) + "cm equivalen a " + str(meters) + " metros")
                os.system("pause")
            case 3:
                kilometers = convertToKilometers(centimeters)
                print("los " + str(centimeters) + "cm equivalen a " + str(kilometers) + " kilometers")
                os.system("pause")
            case 4:
                print("\t\tGracias por usar el programa")
                break
            case _:
                print("opcion no valida")

#**************************************
#  Aqui termina la funcion principal  *
#**************************************