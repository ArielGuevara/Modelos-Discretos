#importacion de la libreria os
import os

def enterKilograms()->float:
    """la funcion valida el ingreso de los kilogramos

    Returns:
        float: kilogramos
    """
    while True:
        try:
            kilograms = float(input("Ingrese los kilogramos: "))
            if kilograms > 0:
                break
            else:
                print("El valor debe ser mayor a cero")
        except:
            print("Debe ingresar solo numeros")

    return kilograms

def convertToPounds(kilograms:float)->float:
    """la funcion convierte los kilogramos a libras

    Args:
        kilograms (float): valor de los kilogramos

    Returns:
        float: conversion de kilogramos a libras
    """
    pounds = kilograms * 2.20462

    return pounds

def convertToGrams(kilograms:float):
    """la funcion convierte los kilogramos a gramos

    Args:
        kilograms (float): valor de los kilogramos

    Returns:
        _type_: conversion de kilogramos a gramos
    """
    grams = kilograms * 1000

    return grams

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
    print("[1] -> Ingresar el valor en kilogramos")
    print("[2] -> Transformar a libras")
    print("[3] -> Transformar a gramos")
    print("[4] -> Salir")

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de variables
    option = int(0)
    kilograms = 0
    pounds = 0
    grams = 0
    while True:
        #limpieza de pantalla
        os.system("cls")
        print("\tBienvenido al sistema para transformar los kilogramos a libras o gramos")
        #llamada a menu
        menu()
        print("\tIngrese una opcion")
        option = validateOption()
        match option:
            case 1:
                kilograms = enterKilograms()
                print("ingreso correcto")
                os.system("pause")
            case 2:
                pounds = convertToPounds(kilograms)
                print("los " + str(kilograms) + "Kg equivalen a " + str(pounds) + " libras")
                os.system("pause")
            case 3:
                grams = convertToGrams(kilograms)
                print("los " + str(kilograms) + "Kg equivalen a " + str(grams) + " gramos")
                os.system("pause")
            case 4:
                print("\t\tGracias por usar el programa")
                break
            case _:
                print("opcion no valida")

#**************************************
#  Aqui termina la funcion principal  *
#**************************************