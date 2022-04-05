def codigos_ascci(cadena):
    """retorna una lista con strings de los cod ascci de cada caracter de la cadena
    """
    lista=list(map(lambda x:ord(x),cadena))
    return lista


def cifrado_Cesar(cadena):
    """retorna la frase con el siguiente de cada caracter de la misma
    """
    caracteres=codigos_ascci(cadena)
    frase=''.join(map(lambda x:chr(x+1),caracteres))
    return frase


print(cifrado_Cesar('abc'))