#Vamos a modificar el código anterior para que imprima la cadena R si la palabra contiene la letra r y sino, imprimal NO TIENE R
for c in range(4):
    cadena=input("Ingrese cadena")
    if "r" in cadena:
        print("TIENE R")
    else:
        print("NO TIENE R")