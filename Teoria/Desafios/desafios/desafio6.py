cadena=input("Ingrese cadena a contar sus letras \"a\": ")
contador=0
for c in cadena:
    if (c=="a"):
        contador+=1
print("Cantidad de letras \"a\" en "+cadena+" es: ",contador)