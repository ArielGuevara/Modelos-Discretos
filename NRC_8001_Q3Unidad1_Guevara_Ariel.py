
#libreria random
import random

#lista de palabras
palabras = ["amarillo", "moneda", "pelota", "electricidad", "playa", "mueble", "azul","rojo",
"mundial", "gato","casa","mesa"]

#muestra la letras acertadas o fallidas asi  de como 
def mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacíos = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

    for letra in espaciosVacíos: # mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()

def obtenerIntento(letrasProbadas):
    # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        #verifica que sean letras lo que se ingresa
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento

def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')

#*********************************
#esta es la funcion principal
#*********************************
if __name__  == '__main__':
    nombre = input("Ingrese su nombre: ")
    letrasIncorrectas = ''
    letrasCorrectas = ''
    #se escoje al azar una palabra de la lista
    palabraSecreta = palabras[random.randint(0,11)]
    juegoTerminado = False
    
    while True:
        mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta)
    
        # Permite al jugador escribir una letra.
        intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
    
        if intento in palabraSecreta:
            letrasCorrectas = letrasCorrectas + intento
    
            # Verifica si el jugador ha ganado.
            encontradoTodasLasLetras = True
            for i in range(len(palabraSecreta)):
                if palabraSecreta[i] not in letrasCorrectas:
                    encontradoTodasLasLetras = False
                    break
            if encontradoTodasLasLetras:
                print('¡Sí! ' + nombre + ' ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
                juegoTerminado = True
        else:
            letrasIncorrectas = letrasIncorrectas + intento
    
            # Comprobar si el jugador ha agotado sus intentos y ha perdido.
            if len(letrasIncorrectas) == 12:
                mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta)
                print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
                juegoTerminado = True
    
        # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
        if juegoTerminado:
            if jugarDeNuevo():
                letrasIncorrectas = ''
                letrasCorrectas = ''
                juegoTerminado = False
                palabraSecreta = palabras[random.randint(0,11)]
            else:
                break

#**********************************
#Aqui termina la funcion principal
#**********************************