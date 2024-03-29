import operator
import csv
#función para abrir los archivos y almacenar sus datos.
#los parámetros de la función son dos: 1.el nombre del archivo y 2.el caracter 
#que separa las columnas (a).
#se considera archivos de dos columnas donde en la primera se encuentra la 
#fecha (en formato dd/mm/aaaa, pudiendose "/" cualquier otro delimitador 
#ej.: ":", "-") y la segunda el precio de las acciones.
def abrir_archivos (archivo, a=","):
    with open (archivo) as archi:
        archi.readline()
        archi=csv.reader(archi, delimiter=a)
        archi=list(archi)
    matriz = [[0]*2 for x in range(len(archi))]
    for x in range(len(archi)):
        matriz[x][0]=archi[x][0]
        matriz[x][1]=float(archi[x][1])
    return matriz   

def variacion_porcentual (inicio, fin):
    "Devuelve la variación porcentual del valor de inicio respecto del valor de fin"
    variacion=(((fin-inicio)/inicio)*100)
    if variacion<0:
        variacion=-variacion
    variacion=round(variacion, 2)
    return variacion

def max_min (matriz, b):
    "Devuelve un valor máximo y uno mínimo respecto de una columna b"
    matriz_ordenada=sorted(matriz, key=operator.itemgetter(b))
    return matriz_ordenada[-1][b], matriz_ordenada[0][b]
