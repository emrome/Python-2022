from urllib import request
from collections import Counter

README_URL = 'https://raw.githubusercontent.com/numpy/numpy/main/README.md'

pagina=request.urlopen(README_URL)

texto = pagina.read().decode('utf-8')
palabras=texto.lower().split()
cont=Counter(palabras)
print(cont.most_common(1))

#print(Counter(texto.lower().split()).most_common(1))