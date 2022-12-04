P = "Puedes salvar calculo vectorial"
Q = "Puedes salvar EDO"

if((P == "Puedes salvar calculo vectorial") or (Q == "Puedes salvar EDO")):
    print("Si Puedo salvar calculo vectorial o si puedo salvar EDO entonces cursare las dos materias" + 
    "(Verdadero)")
elif((P == "Podias salvar calculo vectorial") or (Q == "Puedes salvar EDO")):
    print("Si no Puedo salvar calculo vectorialo si puedo salvar EDO entoncescursare la materia de EDO" + 
    "(Verdadero)")
elif((P == "Puedes salvar calculo vectorial") or (Q == "Podias salvar EDO")):
    print("Si Puedo salvar calculo vectorial o si no puedo salvar EDO entonces cursare la materia de calculo vectorial")
else:
    print("Si no Puedo salvar calculo vectorial o si no puedo salvar EDO entonces no cursare ninguna de las dos  materias")