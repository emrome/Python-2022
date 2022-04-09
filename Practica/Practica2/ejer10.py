
file_nombres=open('nombres_1.txt','r',encoding='utf8')
file_notas_1=open('eval1.txt','r')
file_notas_2=open('eval2.txt','r')
nombres=file_nombres.read()
notas_1=file_notas_1.read()
notas_2=file_notas_2.read()

nombres=nombres.replace(",","").replace("'","").split()
notas_1=notas_1.replace(",","").split()
notas_2=notas_2.replace(",","").split()


notas_total=list(int(n)+int(y) for n,y in zip(notas_2,notas_1))
estudiantes=list(zip(nombres,notas_total))


promedio=0
for n in notas_total: 
    promedio=n+promedio

promedio=promedio/len(notas_total)

print('Alumnos por debajo del promedio')
for pos in range(len(estudiantes)):
    if((estudiantes[pos][1])<promedio):
        print(estudiantes[pos][0])

file_nombres.close()
file_notas_1.close()
file_notas_2.close()