cadena=input("Ingrese una palabra: ")
while cadena != "FIN":
    if cadena[0]== cadena[len(cadena)-1]:
        print(cadena+" empieza y termina con la misma letra")
    else:
        print(cadena+" no empieza y termina con la misma letra")
    cadena=input("Ingrese una palabra: ")