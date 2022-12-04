import random as rd

def generarNumeroRandomico(int_limte)->int:
    """generamos numero randomico

    Args:
        int_limte (entero): es el limte que le daremos a la funcion random

    Returns:
        int: regresa el numero randomico generado
    """
    numero = rd.randint(0,int_limte)#llamado a la fi]uncion randint
    return numero

def etapaJuego(int_numeroEtapa, int_limite)->int:
    """es todo el juego en si, las estapas

    Args:
        int_numeroEtapa (entero): colocara en la etapa en la que nos encpntramos

        int_limite (entero): es el limte que se pasara a generarNumeroRandomico

    Returns:
        bool: devuelve si se logro completar con exito o no las etapas
    """
    intentos = 0
    res =0
    numero = 0
    numero = generarNumeroRandomico(int_limite)#generarmos el nummero randomico
    print("Bienvenidos a la #" + str(int_numeroEtapa))
    while(intentos < 5):
        print("Intenta adivinar el numero")
        res = int(input(">: "))#almacenamos al respuesta del usuario
        if res == numero:#compara si es igual al nuemro
            print("su suposición es correcta")
            return 10
        elif res > numero:#compara si es mayor al numero
            print("Su numero sobrepasa a la respuesta")
        else:#compara si es menor el numero
            print("Su numero es menor a la respuesta")
        intentos += 1
    print("Pierde, Se acabo el juego")
    return False

#******************************
#       Funcion Principal
#********************************

if __name__  == '__main__':
    j = 0
    puntos = 0
    for i in range(0,3):#for que controla las etapas del juego
        if etapaJuego(i+1,(10+j)):
            j += 10
            print("Genial")
        else:
            break;
    if( j == 30):
        print("Ganaste el juego con puntos anotados: " + str(puntos))
#**********************************
#Aqui termina la funcion principal
#**********************************