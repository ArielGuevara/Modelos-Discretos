#libreria random
import random

#lista de palabras
def ecuaciones(int_valor):
    """Genera las ecuaciones a resolver

    Args:
        int_valor (int): es en valor que  designara que ecuacion se usara

    Returns:
        _type_: retorna un float que es la respuesta de la ecuacion
    """
    #generamos numero randomico para a
    a = random.randint(0,10)
    #generamos numero randomico para b
    b = random.randint(1,10)
    #generamos numero randomico para c
    c = random.randint(1,10)
    #generamos numero randomico para d
    d = random.randint(1,10)
    #inicializar variable respuesta
    respuesta = 0
    match int_valor:
        case 1:
            #ecuacion 1
            print("("+str(a)+"+"+str(b)+"+"+str(c)+")mod"+str(d))
            respuesta = ((a+b+c)%d)
            return respuesta
        case 2:
            #ecuacion 2
            print(str(a)+"^"+str(b)+"+"+str(c)+"^"+str(d))
            respuesta = (pow(a,b)+pow(c,d))
            return respuesta
        case 3:
            #ecuacion 3
            print("("+str(a)+"x "+str(b)+"+"+str(c)+")mod"+str(d))
            respuesta = ((a*b+c)%d)
            return respuesta
        case 4:
            #ecuacion 4
            print("("+str(a)+"+"+str(b)+")mod"+str(c)+"+"+str(d))
            respuesta = ((a+b)%c)+d
            return respuesta
        case 5:
            #ecuacion 5
            print("("+str(a)+"x"+str(b)+"-"+str(c)+")"+"x"+str(d))
            respuesta = (a*b-c)*d
            return respuesta
        case 6:
            #ecuacion 6
            print(str(a)+" x -"+str(b)+"+"+str(c)+" x -"+str(d))
            respuesta = a*(-b) + c*(-d)
            return respuesta
        case 7:
            #ecuacion 7
            print(str(a)+"+"+str(b)+"-"+str(c)+"+"+str(d))
            respuesta = a+b-c+d
            return respuesta
        case 8:
            #ecuacion 8
            print("("+str(a)+" mod "+str(b)+")"+"+ ("+str(c)+" mod "+str(d)+")")
            respuesta = (a%b) + (c%d)
            return respuesta


def jugarDeNuevo():
    """Pregunta si el usuario quiere volver a jugar

    Returns:
        bool: si es True vuelve a jugar, si es False termina
    """
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')
    

#*********************************
#esta es la función principal
#*********************************
if __name__  == '__main__':
    #declaracion de la variale vida
    vida = float(0)
    #declaracion de la variable rondas
    rondas = float(0)
    #Declaracionde la variable numRondas
    numRondas = int(1)
    #ingreso de nombre
    nombre = input("Ingrese su nombre: ")
    #while se ejecuta mientras se cumpla una de las proposiciones
    while (vida < 3) and (rondas < 10):
        #se genera numero randomico el cual elige que ecuacion se resolvera
        rand = random.randint(0,8)
        print("\t\t  Ronda #"+str(numRondas)+" de 10")
        #llamamos ala funcion que genera las ecuaciones
        valor = ecuaciones(rand)
        #captura de algun tipo de error
        try: 
            respuesta = float(input("Ingrese su respuesta: "))
        except:
            print("\t\t*Debes ingresar numeros*")
            #valor = ecuaciones(rand)
            respuesta = float(input("Ingrese su respuesta: "))
        #valida si es correcta la respuesta
        if(valor == respuesta):
            print("Correcto "+nombre+ ", pasas a la siguiente ronda")
            rondas += 1
            numRondas += 1
        else:
            print("Incorrecto "+nombre+ ", intentalo otra vez")
            vida += 1
    #cuando llega al maximo de sus vidas
    if(vida == 3):
        print("te quedaste sin vidas")
    else:
        print("Ganaste terminaste las 10 rondas")

    while jugarDeNuevo():#validamoso si queremos volver a jugar
        #declaracion de la variale vida
        vida = float(0)
        #declaracion de la variable rondas
        rondas = float(0)
        #Declaracionde la variable numRondas
        numRondas = int(1)
        #ingreso de nombre
        nombre = input("Ingrese su nombre: ")
        #while se ejecuta mientras se cumpla una de las proposiciones
        while (vida < 3) and (rondas < 10):
            #se genera numero randomico el cual elige que ecuacion se reslvera
            rand = random.randint(0,8)
            #llamado a las ecuaciones
            valor = ecuaciones(rand)
            #captura de algun tipo de error
            try: 
                respuesta = float(input("Ingrese su respuesta: "))
            except:
                print("\t\t*Debes ingresar numeros*")
                valor = ecuaciones(rand)
                respuesta = float(input("Ingrese su respuesta: "))

            if(valor == respuesta):
                print("Correcto "+nombre+ ", pasas a la siguiente ronda")
                rondas += 1
            else:
                print("Incorrecto "+nombre+ ", intentalo otra vez")
                vida += 1

        if(vida == 3):
            print("te quedaste sin vidas")
        else:
            print("Ganaste terminaste las 10 rondas")


#**************************************
#  Aqui termina la funcion principal  *
#**************************************