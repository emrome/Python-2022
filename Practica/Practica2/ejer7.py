from collections import Counter
from string import ascii_letters

def sacar_especiales(aux):  #se puede hacer solo en el join??
    caracteres=""
    for n in aux:
        if n in ascii_letters:
          caracteres+="".join(n)
    return caracteres

entrada=input("Ingrese frase o palabra a verificar si es Heteorgrama: ").lower()

letras=sacar_especiales(entrada)

if len (letras)== len(set(letras)):
    print("Es un heterograma")
else:
    print("No es un heterograma")