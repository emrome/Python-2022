def ordeno(cadena):
    """retorna una lista con las palabras de la cadena recibida en orden alfabético
    """
    palabras=cadena.lower().split()
    palabras.sort(key=str.lower)
    return set(palabras)

print(ordeno("Hoy hoy puede ser un gran día. "))