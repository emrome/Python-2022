def separar_nombres(a):
    """
    Recibe un string y separa por lineas, sacandole comas y comillas  
    """
    a=a.replace(",","").replace("'","").split()
    return a

def separar(arc):
    arc=arc.replace(",","").split()

    return list(map((lambda x:int(x)),arc))


nombres_1=open('nombres_1.txt','r',encoding='utf8').read()
nombres_1=separar_nombres(nombres_1)

nombres_2=open('nombres_2.txt','r',encoding='utf8').read()
nombres_2=separar_nombres(nombres_2)
repetidos=set(filter((lambda x: x in nombres_2),nombres_1))
print(repetidos)


notas_1=open('eval1.txt','r').read()
notas_1=separar(notas_1)
notas_2=open('eval2.txt','r').read()
notas_2=separar(notas_2)

print('     {:<15} {:<8}{:<8}{:<8}'.format('Nombre','Eval1','Eval2','Total'))
for i in range(len(nombres_1)):
    print(' {:<2}  {:<15} {:<8}{:<8}{:<8}'.format(i,nombres_1[i],notas_1[i],notas_2[i],(notas_1[i]+notas_2[i])))
