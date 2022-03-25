#Necesitamos procesar las notas de los estudiantes de este curso. Queremos saber: 
#¿Cúal es el promedio de las notas?
#¿Qué estudiantes están por debajo del promedio?
def ingreso_notas():
    nombre = input("Ingresa un nombre (<FIN> para finalizar): ")
    dicci = {}
    while nombre != "FIN":
        nota = int(input(f"Ingresa la nota de {nombre}: "))
        dicci[nombre] = nota
        nombre = input("Ingresa un nombre (<FIN> para finalizar): ")
    return dicci

notas_de_estudiantes=ingreso_notas()

acumulador=0
for n in notas_de_estudiantes.values():
    acumulador+=n
promedio=acumulador/len(notas_de_estudiantes)
estudiantes_debajo_promedio = []
for alumno in notas_de_estudiantes:
    if notas_de_estudiantes[alumno]<promedio:
        estudiantes_debajo_promedio.append(alumno)

print("Promedio de notas: {:.2f}".format(promedio))
print("Lista de estudiantes por debajo del promedio ")
for elem in estudiantes_debajo_promedio:
    print(elem+"\n")
