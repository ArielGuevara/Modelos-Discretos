#importacion de la libreria os
import os

def validateNumbers()->float:
    while True:
        try:
            number = float(input("Ingrese el numero: "))
            break
        except:
            print("Debe ingresar solo numeros")
    return number
    
def validateRange()->int:
    while True:
        try:
            number = int(input("Ingrese cuantos numeros desea operar: "))
            break
        except:
            print("Debe ingresar solo numeros")
    return number

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

def addition(limite:int)->float:
    lista = []
    result = 0
    #ingreso de numeros
    for element in range(0,limite):
        lista.append(validateNumbers())

    #suma de los numeros
    for element in lista:
        result += element
    
    return result

def multiplication(limite:int)->float:
    lista = []
    result = 1
    #ingreso de numeros
    for element in range(0,limite):
        lista.append(validateNumbers())

    #suma de los numeros
    for element in lista:
        result *= element
    
    return result

def division(limite:int)->float:
    lista = []
    result = 0
    #ingreso de numeros
    for element in range(0,limite):
        lista.append(validateNumbers())
    
    if limite == 1:
        return lista[0]
    elif limite == 2:
        try:
            result = lista[0]/lista[1]
        except:
            print("no se puede realizar la division entre 0")
    else:
        try:
            result = lista[0]/lista[1]
            for i in range(2,limite):
                result = result/lista[i]
        except:
            print("no se puede realizar la division entre 0")


    return result

def integerDivision(limite:int)->float:
    lista = []
    result = 0
    #ingreso de numeros
    for element in range(0,limite):
        lista.append(validateNumbers())
    
    if limite == 1:
        return lista[0]
    elif limite == 2:
        try:
            result = lista[0]%lista[1]
        except:
            print("no se puede realizar la division entre 0")
    else:
        try:
            result = lista[0]%lista[1]
            for i in range(2,limite):
                result = result%lista[i]
        except:
            print("no se puede realizar la division entre 0")


    return result

def empowerment()->float:
    while True:
        try:
            base = float(input("Ingrese el valor de la base: "))
            break
        except:
            print("Debe ingresar solo numeros")

    while True:
        try:
            print("\t\tEl exponente no debe ser mayo a 100 o menor a -100")
            exponent = float(input("Ingrese el exponente: "))
            if exponent > -100 and exponent < 100:
                break
            else:
                print("El valor ingresado sobrepasa el rango preestablecido")
        except:
            print("Debe ingresar solo numeros")

    return (base**exponent)

def substraction(limite:int)->float:
    lista = []
    result = 0
    #ingreso de numeros
    for element in range(0,limite):
        lista.append(validateNumbers())

    #resta de los numeros
    for element in lista:
        result -= element
    
    return result

def menu():
    """devuelve el menu disponible
    """
    print("*********************************")
    print("*\t\tMENU\t\t*")
    print("*********************************")
    print("[1] -> Sumar")
    print("[2] -> Restar")
    print("[3] -> Multiplicar")
    print("[4] -> Dividir")
    print("[5] -> Divison entera")
    print("[6] -> Potenciacion")
    print("[7] -> Salir")

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #incializacion de variables
    option = 0
    limite = 0

    #ciclo del menu
    while True:
        #limpieza de pantalla
        os.system("cls")
        print("\tBienvenido al sistema para operaciones aritmeticas")
        #llamada a menu
        menu()
        print("\tIngrese una opcion")
        option = validateOption()
        match option:
            case 1:
                #ingreso de la cantidad de numeros a operar
                limite = validateRange()
                print("El resultado de la suma es: {}".format(addition(limite)))
                #pausa para visualizar las respuestas
                os.system("pause")
            case 2:
                #ingreso de la cantidad de numeros a operar
                limite = validateRange()
                print("El resultado de la resta es: {}".format(substraction(limite)))
                #pausa para visualizar las respuestas
                os.system("pause")
            case 3:
                #ingreso de la cantidad de numeros a operar
                limite = validateRange()
                print("El resultado de la multiplicacion es: {}".format(multiplication(limite)))
                os.system("pause")
            case 4:
                #ingreso de la cantidad de numeros a operar
                limite = validateRange()
                print("El resultado de la division es: {}".format(division(limite)))
                #pausa para visualizar las respuestas
                os.system("pause")
            case 5:
                #ingreso de la cantidad de numeros a operar
                limite = validateRange()
                print("El resultado de la division entera es: {}".format(integerDivision(limite)))
                #pausa para visualizar las respuestas
                os.system("pause")
            
            case 6:

                print("El resultado de la exponenciacion es: {}".format(empowerment()))
                #pausa para visualizar las respuestas
                os.system("pause")
            case 7:
                #salida
                print("\t\tGracias por usar el programa")
                break
            case _:
                #caso erroneo
                print("opcion no valida")
#**************************************
#  Aqui termina la funcion principal  *
#**************************************