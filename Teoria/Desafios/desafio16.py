import csv
import os
from collections import Counter


ruta_completa =os.getcwd()
ruta_archivo_netflix =os.path.join(ruta_completa, "netflix_titles.csv")
ruta_peliculas_2021=os.path.join(ruta_completa, "peliculas_2021.csv")

archivo_netflix=open(ruta_archivo_netflix, encoding='utf-8')
archivo_peliculas=open(ruta_peliculas_2021,'w',encoding='utf-8')

reader=csv.reader(archivo_netflix, delimiter=',')
writer=csv.writer(archivo_peliculas)
writer.writerow(next(reader))
paises={}

for linea in reader:
    if linea[7]=="2021" and linea[1]=="Movie":
        writer.writerow(linea)
    if linea[5] in paises.keys():
        paises[linea[5]]+=1
    else:
        paises[linea[5]]=1
del paises['']
top_5=dict(Counter(paises).most_common(5))
print('Los 5 paises con más titulos: ')
print(top_5)

archivo_netflix.close()
archivo_peliculas.close()
