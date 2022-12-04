P = "Si es un dia feriado"
Q = "tendremos vacaiones"

# V - V
if(P == "Si es un dia feriado"):
    print("tendremos vacaiones (Verdadero)")
#********************************************
# V - F
if(P == "Si es un dia feriado"):
    print("tendremos clases (Falso)")
#***************************************
# F - V
if(P == "Si es un dia conmemorativo"):
    print("tendremos vacaiones (Verdadero)")

#***************************************
# F -F 
if(P == "Si es un dia conmemorativo"):
    print("tendremos clases (Verdadero)")
    