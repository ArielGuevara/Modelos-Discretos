P = "Si tengo material de construcción"
Q = " tengo un terreno"

if( not P == "Si no tengo material de construcción") and (not Q == " no tengo un terreno"):
    # v - v
    print("Si no tengo material de construcción y no tengo un terreno entonces no puedo construir mi casa "+
        "(Verdadero)")
elif(not P == "Si no tuviera material construcción") and (not Q == "no tengo un terreno"):
    # F- V
    print("Si no tuviera material de construcción Y no tengo un terreno entonces no puedo construir mi casa " + 
        "(Falso)")
elif(not P == "Si no tengo material de construcción") and (not Q == "no tuviera un terreno"):
    #V-F
    print("Si no tengo material de construcción y no tuviera un terreno entonces no puedo construir mi casa" + 
    "(Falso)")
else:
    #F-F
    print("Si no tuviera material de construcción y no tuviera un terreno entonces no puedo construir mi casa" + 
    "(Falso)")