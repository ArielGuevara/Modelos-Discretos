P = "Si tengo material de construcción"
Q = " tengo un terreno"

if(P == "Si tengo material de construcción") and (Q == " tengo un terreno"):
    # v - v
    print("Si tengo material de construcción y tengo un terreno entonces puedo construir mi casa "+
        "(Verdadero)")
elif(P == "Si tuviera material construcción") and (Q == "tengo un terreno"):
    # F- V
    print("Si tuviera material de construcción Y tengo un terreno entonces no puedo construir mi casa " + 
        "(Falso)")
elif(P == "Si tengo material de construcción") and (Q == "tuviera un terreno"):
    #V-F
    print("Si tengo material de construcción y tuviera un terreno entonces no puedo construir mi casa" + 
    "(Falso)")
else:
    #F-F
    print("Si tuviera material de construcción y tuviera un terreno entonces no puedo construir mi casa" + 
    "(Falso)")