def hoursWorker()->int:
    """esta funcion permite ingresar las horas trabajadas

    Returns:
        int: las horas trabajadas
    """
    #ingreso de las horas a la variable hours
    hours = input("¿Cuántas horas ha trabajado?: ")
    #retorno de las variables hourd
    return hours 

def costPerHour(hours:int)->float:
    """la funcion calcula el costo por hora

    Args:
        hours (int): las horas trabajadas

    Returns:
        float: el total del costo por hora
    """
    #ingreso del valor del costo por hora
    cost = float(input("Ingrese el costo por hora: "))
    #calculo del costo por hora
    total = hours * cost
    #retorno del calculo
    return total 

#*********************************
#  Esta es la función principal  *
#*********************************
if __name__ == "__main__":
    #inicializacion de las variables
    cost = 0
    hours = 0
    #impresion de las instrucciones
    print("*" * 80)
    print("*\tBienvenido al programa para calcular el costo por hora trabajada\t*")
    print("* 1._ Debera ingresar las horas que ha trabajado\t\t\t\t*")
    print("* 2._ Debera ingresar el costo por de cada hora\t\t\t\t\t*")
    print("*" * 80)
    #ciclo de validacion para el ingreso de las horas trabajadas
    while True:
        #captura de errores
        try:
            #ingreso de las horas trabadas
            hours = int(hoursWorker())
            #validacion de horas trabajadas
            if hours >= 0:
                #se rompe el ciclo el while
                break
            else:
                print("El valor debe ser numerico y mayor a cero")
        except:
            print("Solo debe ingresar numeros")
    #captura de errores
    while True:
        try:
            #ingreso del costo por hora
            cost = float(costPerHour(hours))
            if cost > 0:
                #se rompe el ciclo el while
                break
            else:
                print("El costo debe ser numerico y mayor a cero")
        except:
            print("Solo debe ingresar numeros")
    #se muestra el resultado de los valores ingresados
    print("El costo por " + str(hours) + " horas es de: " + str(cost) + "$")
#**************************************
#  Aqui termina la funcion principal  *
#**************************************