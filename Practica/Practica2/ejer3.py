import string
texto = """The constants defined in this module are:The constants defined in␣
,→this module are:
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants␣
,→described below. This value is not locale-dependent.
string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not␣
,→locale-dependent and will not change.
string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not␣
,→locale-dependent and will not change.
"""

caracter=input("Ingrese letra ")
if caracter in string.ascii_letters:
    caracter.lower()
    palabras=texto.lower().split()
    for n in palabras: 
        if n.startswith(caracter):
            print(n) 