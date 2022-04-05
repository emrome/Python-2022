from collections import Counter
import  string 
frase=input("Ingrese una frase: ").lower()
palabra=input("Ingrese palabra a contar cantidad: ").lower()


frase=frase.replace(",","").replace(".","") #como reemplzar todos los caracteres especiales

cant=Counter(frase.split())[palabra]

print(f"{palabra} se encuentra {cant} veces en \"{frase}\"")


"""Informa si los caracteres “@” o “!” formaban
parte de una palabra ingresada
"""

cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !): ")
if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
elif ("@" in cadena) or ("!" in cadena):
    print("Ingresaste alguno de estos símbolos: @ o !" )
else:
    print("Clave válida")
