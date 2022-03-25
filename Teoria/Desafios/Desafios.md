# <h1 align="center"> Desafios </h1>

## ```Desafio 1 ```[Resolución](#Desafio_1)

* Queremos ingresar un número desde teclado e imprimir si el número es o no par.
* ¿Cómo sería el pseudocódigo de esto?
```
Ingresar un número desde teclado
SI es par: 
    Mostrar mensaje: "es par"
SINO:
    Mostrar mensaje: "NO es par"
```
## ```Desafio 2``` [Resolución](#Desafio_2)
* Queremos ingresar un número desde el teclado e imprimir si es múltiplo de 2,3 o 5.
* **Pista**: Python tiene otra forma de la sentencia condicional: if-elif-else

## ```Desafio 3``` [Resolución](#Desafio_3)
* Dado una letra ingresada por el teclado, queremos saber si es mayúscula o minúscula.

## ```Desafio 4 ```[Resolución](#Desafio_4)
* Dado un caracter ingresado por el teclado, queremos saber si es una comilla o no.
¿Hay algún problema?

## ```Desafio 5``` [Resolución](#Desafio_5)
* Dadas dos cadenas ingresadas desde el teclado, imprimir aquella que tenga más caracteres.

## ```Desafio 6``` [Resolución](#Desafio_6)
* Escribir un programa que ingrese desde teclado una cadena de caracteres e imprima cuántas letras a contiene.

## ```Desafio 7``` [Resolución](#Desafio_7)
* Escribir un programa que ingrese 4 palabras desde teclado e imprima aquellas que contienen la letra r.
* **Pensar**: ¿Podemos usar la instrucción for tal cual la vimos la clase pasada para las 4 iteraciones?
* La sentencia for permite iterar sobre una secuencia.

## ```Desafio 8 ```[Resolución](#Desafio_8)
* Vamos a modificar el código anterior para que imprima la cadena R si la palabra contiene la letra r y sino, imprimal NO TIENE R

## ```Desafio 9 ```[Resolución](#Desafio_9)
* Ingresar palabras desde teclado hasta ingresar la palabra FIN. Imprimir aquellas que empiecen y terminen con la misma letra

* ¿Qué estructura de control deberiamos utilizar para realizar esta interación?¿Podemos utilizar la sentencia for?

## ```Desafio 10 ```[Resolución](#Desafio_10)
**Necesitamos procesar las notas de los estudiantes de este curso. Queremos saber:**

* Cuál es el promedio de las notas
* Cuántos estudiantes están por debajo del promedio
```
Ingresar las notas
Calcular el promedio
Calcular cuántos tienen notas menores al promedio

```
* Empecemos con el primer proceso: vamos a suponer que ingresamos datos hasta que ingrese una nota -1

## ```Desafio 11 ```[Resolución](#Desafio_11)
**Necesitamos procesar las notas de los estudiantes de este curso. Queremos saber:** 

* ¿Cúal es el promedio de las notas?
* ¿Qué estudiantes están por debajo del promedio?
* ¿Qué diferencia hay con el desafio anterior?

* Deberíamos ingresar no sólo las notas, sino también los nombres de los estudiantes.
¿Qué soluciones proponen?

# Desafio_1
```Py
num=int(input("Ingrese un numero: "))
if num % 2 == 0:
    print("Es PAR")
else:
    print("Es IMPAR")
```
# Desafio_2
```Py
num=int(input("Ingrese un numero: "))
if num % 2 == 0:
    print("Es multiplo de 2")
elif num % 3 == 0:
    print("Es mulitplo de 3")
elif num % 5 == 0:
    print("Es multiplo de 5")
else:
    print("No es multiplo de 2, 3 o 5")
```
# Desafio_3
```Py
letra=input("Ingrese una letra: ")
if ((letra >="a") and (letra<="z")):
    print("Es minuscula")
elif ((letra >="A") and (letra<="z")):
    print("Es mayuscula")
else:
    print("No es una letra")
```
# Desafio_4
```Py
caracter=input("Ingrese un caracter: ")
if caracter=="\"":
    print("El caracter es una comilla")
else:
    print("No es comilla")
```
# Desafio_5
```Py
cadena1=input("Ingrese la primera cadena: ")
cadena2=input("Ingrese la segunda cadena: ")
if len(cadena1)>len(cadena2):
    print("La cadena \""+cadena1+"\" tiene mas caracteres que la cadena \""+cadena2+"\"")
elif len(cadena1)<len(cadena2):
    print("La cadena \""+cadena2+"\" tiene mas caracteres que la cadena \""+cadena1+"\"")
else: 
    print("Las cadenas tienen la misma cantidad de caracteres")
```

# Desafio_6
```Py
cadena=input("Ingrese cadena a contar sus letras \"a\": ")
contador=0
for c in cadena:
    if (c=="a"):
        contador+=1
print("Cantidad de letras \"a\" en "+cadena+" es: ",contador)
```

# Desafio_7
```Py
for c in range(4):
    cadena=input("Ingrese una cadena: ")
    if "r" in cadena:
        print("La cadena \"{}\" contiene r".format(cadena))
```

# Desafio_8
```Py
for c in range(4):
    cadena=input("Ingrese cadena")
    if "r" in cadena:
        print("TIENE R")
    else:
        print("NO TIENE R")
```

# Desafio_9
```Py
cadena=input("Ingrese una palabra: ")
while cadena != "FIN":
    if cadena[0]== cadena[len(cadena)-1]:
        print(cadena+" empieza y termina con la misma letra")
    else:
        print(cadena+" no empieza y termina con la misma letra")
    cadena=input("Ingrese una palabra: ")
```

# Desafio_10
```Py
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
```

# Desafio_11
```Py
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
```

