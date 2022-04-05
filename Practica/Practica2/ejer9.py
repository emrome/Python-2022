
def setearMapa(minas):
    """"Esta funcion recibe la estructura de las minas y setea el mapa con los casillero de bombas 
    y los casilleros que la rodean en '0'
    Por ej:   minas=[['-','*','-','*','-'],['-','-','*','-','-'],['-','-','-','-','*'],['*','-','-','-','-']] ->
              mapa=[['0','*','0','*','0'],['0','0','*','0','0'],['0','0','0','0','*'],['*','0','0','0','0']]
    """
    mapa=[]
    for fila in minas:
        lista=[]
        for col in fila:
            if (col=='*'):
                lista.append(col)
            else:
                lista.append('0')
        mapa.append(lista)
    
    return mapa

def incrementar(mapa,fila,col):
    """Esta funcion recibe el mapa de informacion y las coordenadas de un casillero cercano a una bomba 
    e incrementa la cantidad de bombas cercanas a el 
    """
    if((0<=fila<len(mapa))and(0<=col<len(mapa[fila]))):
        if(mapa[fila][col]!='*'): #el casillero cercano puede ser una bomba
            mapa[fila][col]=str(int(mapa[fila][col])+1)

            
def bombas(mapa,fila,pos):
    """"Esta funcion recibe el mapa de info y las coordenadas donde hay una bomba e incrementa los casilleros
    cercanos sin bomba
    """
    for f in range((fila-1),(fila+2)):
        for j in range((pos-1),(pos+2)):
            incrementar(mapa,f,j)



def generarMapa(minas):
    """"Esta funcion recibe la minas y devuelve una lista con las celdas vacias seteadas
    en la cantidad de bombas que lo rodean
    """
    mapa=setearMapa(minas)
    
    for fila in range(len(mapa)):
        for pos in range(len(mapa[fila])):
            if(minas[fila][pos])=='*':
                bombas(mapa,fila,pos)
                
    for j in range(len(mapa)):
        mapa[j]=''.join(mapa[j])

    return mapa

   
minas=['-*---','--*--','----*','*----',]
print(minas)

minas=[list(fila) for fila in minas] 
buscaminas=generarMapa(minas)
print(buscaminas)