#INSTRUCTIONS
#Enter LOCATION A/B in captial letters
#Enter Status O/1 accordingly where 0 means CLEAN and 1 means DIRTY

def Aspiradora():
    """
    Este es un procedimiento para emular el funcionamiento de una aspiradora
    Atributos:
    -------
    No tiene parametros de entrada

    return
    -------
    No retorna ningun valor
    """
    # initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    #declara variable objetivo
    goal_state = {'A': '0', 'B': '0'}
    #inicializa variable costo en cero
    cost = 0
    #ingresa Valor en location_input quien recibe el valor que valida la habitacion
    #en la que nos encontramos
    location_input = input("Enter Location of Vacuum: ") #user_input of location vacuum is placed
    #ingresa Valor en location_input quien recibe el valor que valida si esta limpio o sucia la habitacion
    status_input = input("Enter status of: " + location_input) #user_input if location is dirty or clean
    #status_input_complement guarda el estaod actual de la habitacion
    status_input_complement = input("Enter status of other room: ")
    #nos indica los estados y su codigo de las habitaciones
    print("Desired Goal:" + str(goal_state))

    # Este if nos ubica en la habitacion que nos encontramos
    if location_input == 'A':
        # Location A is Dirty.
        #nos indica que estamos en la habitacon A
        print("Vacuum is placed in Location A: ")
        #este if valida si el cuarto esta limpio o sucio
        if status_input == '1':
            #nos avisa que la habitacion A esta sucia
            print("Location A is Dirty.")
            # suck the dirt  and mark it as clean
            #Si en goal_state A es 0 incrementa en 1 el costo
            goal_state['A'] = '0'
            cost += 1## increasing cost for cleaning A
            #nos indica que A esta limpia
            print("Cleaning location A")
            #imprime el valor de la variable costo
            print("Current Cost: " + str(cost))

            #Vemos el estado actual de la habitacion
            if status_input_complement == '1':
                # if B is Dirty
                #indica el estado da la habitacion B
                print("Location B is Dirty.")
                print("Moving right to the Location B. ")
                #aumenta en 1 la variable costo
                cost += 1 #increasing cost for moving right
                print("Current cost: " + str(cost))
                # suck the dirt and mark it as clean
                #Mira si B es igual cero 
                goal_state['B'] = '0'
                #aumenta en 1 la variable costo
                cost += 1 #increasing cost for cleaning
                #indica que se impio la habotacion B
                print("Cleaning location B")
                #imprime el valor de costo
                print("Current cost: " + str(cost))
            else:
                # suck and mark clean
                print("Location B is already clean.")
                print("No action. Current cost" + str(cost))              
        if status_input == '0':
            print("Location A is already clean.")
            if status_input_complement == '1':# if B is Dirty
                print("Location B is Dirty.")
                print("Moving RIGHT to the Location B.")
                cost += 1 #increasing cost for moving right
                print("Current cost: " + str(cost))
                # suck the dirt and mark it as clean
                #mira si B es igual a cero 
                goal_state['B'] = '0'
                #aumenta en 1 la variable costo
                cost += 1   
                print("Cleaning location B. ")                    #cost for suck
                print("Updated cost: "+str(cost))
                
            else:
                #aqui indica que no hubo action sobre la variable costo
                print("No action " + str(cost))
                print(cost)
                # suck and mark clean
                print("Location B is already clean.")

    else:
        #El vacío se coloca en la ubicación B
        print("Vacuum is placed in location B")
        # Location B is Dirty.
        # mira el estado de B si esta sucia 
        if status_input == '1':
            print("Location B is Dirty.")
            # suck the dirt  and mark it as clean
            #mira si B es igual  cero
            goal_state['B'] = '0'
            #aumenta en 1 la variable costo
            cost += 1  # cost for suck
            print("COST for CLEANING " + str(cost))
            print("Location B has been Cleaned.")

            #mira el estado si es uno significa que etsa sucio
            if status_input_complement == '1':
                # if A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1  # cost for moving right
                print("COST for moving LEFT" + str(cost))
                # suck the dirt and mark it as clean
                #mira si A es igual a CERO
                goal_state['A'] = '0'
                #aumenta en uno la variable costo
                cost += 1  # cost for suck
                #indica el costo por la aspirada
                print("COST for SUCK " + str(cost))
                print("Location A has been Cleaned.")

        else:
            #imprime la variable costo
            print(cost)
            # suck and mark clean
            print("Location B is already clean.")

            #verifica el estado si es igual a 1 siginifa que A esta sucia
            if status_input_complement == '1':  # if A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                #aumenta en uno la variable costo
                cost += 1  # cost for moving right
                print("COST for moving LEFT " + str(cost))
                # suck the dirt and mark it as clean
                #verifica que la variable A es igual a cero
                goal_state['A'] = '0'
                #aumenta en uno la variable costo
                cost += 1  # cost for suck
                print("Cost for SUCK " + str(cost))
                print("Location A has been Cleaned. ")
            else:
                #indica que no se hace ninnguna accion
                print("No action " + str(cost))
                # suck and mark clean
                print("Location A is already clean.")

    # done cleaning
    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))

#definimos el main o funcion prncipal donde se ejecutaran las funciones
if __name__  == '__main__':
    #llamamos a la funcion aspiradora
    Aspiradora()