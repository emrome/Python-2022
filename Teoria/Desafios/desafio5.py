cadena1=input("Ingrese la primera cadena: ")
cadena2=input("Ingrese la segunda cadena: ")
if len(cadena1)>len(cadena2):
    print("La cadena \""+cadena1+"\" tiene mas caracteres que la cadena \""+cadena2+"\"")
elif len(cadena1)<len(cadena2):
    print("La cadena \""+cadena2+"\" tiene mas caracteres que la cadena \""+cadena1+"\"")
else: 
    print("Las cadenas tienen la misma cantidad de caracteres")