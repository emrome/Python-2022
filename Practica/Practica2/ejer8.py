
uno=["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
dos= ["D", "G"]
tres = ["B", " C", "M", "P"]
cuatro = ["F", "H", "V", "W", "Y "]
cinco = ["K"]
ocho = ["J", "X "]
diez = ["Q", "Z "]

puntaje={c:1 for c in uno}
puntaje.update({c:2 for c in dos})
puntaje.update({c:3 for c in tres})
puntaje.update({c:4 for c in cuatro})
puntaje.update({c:5 for c in cinco})
puntaje.update({c:8 for c in ocho})
puntaje.update({c:10 for c in diez})


print(type(puntaje))
print(puntaje)
palabra=input("Escriba una palabra para conocer sus puntos: ").upper()
puntos=0
for letra in palabra:
   puntos+=puntaje[letra]

print(f"Puntaje de la palabra {palabra}: {puntos}")