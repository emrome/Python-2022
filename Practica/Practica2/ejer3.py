from string import ascii_letters

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
if caracter in ascii_letters:
    caracter.lower()
    for n in texto.lower().split(): 
        if n.startswith(caracter):
            print(n) 
else:
    print("El caracter no es una letra")