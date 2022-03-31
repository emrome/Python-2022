from urllib import request

README_URL = 'https://raw.githubusercontent.com/numpy/numpy/main/README.md'

pagina=request.urlopen(README_URL)

texto = pagina.read().decode('utf-8')
lineas = texto.splitlines()
lineas_con_http=filter(lambda l: "http" in l,lineas)

for linea in lineas_con_http:
    print(linea)

#for linea in lineas:
#   if "http" in linea:
#       print(linea)