#Cuál es el promedio de las notas
#Cuántos estudiantes están por debajo del promedio

nota = int(input("Ingresá una nota (-1 para finalizar): "))
acumulador=0
lista_de_notas = []

while nota != -1:
    acumulador+=nota
    lista_de_notas.append(nota)
    nota = int(input("Ingresá una nota (-1 para finalizar): "))

promedio=acumulador/len(lista_de_notas)

estudiantes_debajo_promedio=0

for indice in range(len(lista_de_notas)):
    if lista_de_notas[indice]<promedio:
        estudiantes_debajo_promedio+=1


print("Promedio de notas: {:.2f}".format(promedio))
print("Cantidad de estudiantes por debajo del promedio: ",estudiantes_debajo_promedio)