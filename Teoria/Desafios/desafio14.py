def ordeno_usuarios(usuarios):
    """retorna la colección recibida ordenada de acuerdo al nombre.
    """
    return sorted (usuarios,key=lambda usuario: usuario[0])


usuarios = [
('JonY BoY', 'Nivel3', 15),
('1962', 'Nivel1', 12),
('caike', 'Nivel2', 1020),
('Straka^', 'Nivel2', 1020),
]
print(ordeno_usuarios(usuarios))