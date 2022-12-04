# initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
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
    #declara variable objetivo
    goal_state = {'A': '0', 'B': '0'}
    #inicializa variable costo en cero
    cost = 0

    location_input = input("Enter Location of Vacuum: ") #user_input of location vacuum is placed
    status_input = input("Enter status of: " + location_input) #user_input if location is dirty or clean
    status_input_complement = input("Enter status of other room: ")
    print("Desired Goal:" + str(goal_state))

if __name__  == '__main__':
    Aspiradora()