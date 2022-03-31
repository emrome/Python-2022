texto=""" título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python 
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""
analisis={"titulo":"","faciles":0, "aceptables":0, "dificiles":0, "muy_dificiles":0}

titulo=texto.split("resumen: ")[0]
resumen=texto.split("resumen: ")[1]

if len(titulo.split())<=11:
    analisis["titulo"]="ok"
else: 
    analisis["titulo"]="no ok"


oraciones=resumen.split(".")
for oracion in oraciones:
    palabras=len(oracion.split())
    match palabras:
        case palabras if palabras<13:
            analisis["faciles"]+=1
        case palabras if 12<palabras<18:
            analisis["aceptables"]+=1
        case palabras if 17<palabras<26:
            analisis["dificiles"]+=1
        case palabras if palabras>25:
            analisis["muy_dificiles"]+=1

print("ANALISIS: ")
print(analisis)