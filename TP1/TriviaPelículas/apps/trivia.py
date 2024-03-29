import random
import datetime
import csv
from modulos.modulos import frases_random
import operator

with open ("./data/frases_de_peliculas.txt", encoding="utf-8") as archivo:
  archi=csv.reader(archivo, delimiter=";")
  peliculas=list(archi)

matriz=[[0]*2 for x in range(len(peliculas))]
for x in range(len(peliculas)):
  matriz[x][0]=peliculas[x][0]
  matriz[x][1]=peliculas[x][1]

menu="""
#######################################
#  Películas: Preguntas y respuestas  #
#######################################
Elige una opción
1 - Mostrar lista de películas.
2 - ¡Trivia de película!
3 - Mostrar secuencia de opciones seleccionadas previamente.
4 - Borrar historial de opciones.
5 - Salir
"""

salir=False

lista=[]

try:
    with open ("./data.registro_opciones.txt") as file:
        file=csv.reader(file, delimiter=",")
        file=list(file)
        for x in file:
            lista.append([x[0], x[1]])
except FileNotFoundError:
    pass

while not salir:
    option=input(menu)
    if option=="1":
        lista.append([1, (str(datetime.datetime.now())[:19])])
        matriz.sort(key=operator.itemgetter(1))
        try:
            for x in range(len(matriz)):
              if matriz[x][1]!=matriz[x+1][1]:
                print(matriz[x+1][1])
              else:
                 pass
        except IndexError:
          pass
    elif option=="2":
        lista.append([2, (str(datetime.datetime.now())[:19])])
        triplete=frases_random(matriz)
        x=random.randint(0,2)
        opciones=f"""
        ¿De qué película es la frase {triplete[x][0]}?
         1-{triplete[0][1]}
         2-{triplete[1][1]}
         3-{triplete[2][1]}
         """
        try:
           electa=int(input(opciones))
        except ValueError:
           print("Esa no es una de las opciones.")

        if x==0:
           correcta=1
        elif x==1:
          correcta=2
        else:
          correcta=3
      
        if correcta==electa:
          print("Correcto, ¡felicitaciones!")
        else:
          print(f"Incorrecto. La respuesta correcta era la opción {correcta}")
          
    elif option=="3":
        lista.append([3, (str(datetime.datetime.now())[:19])])
        for x in range(len(lista)):
          print(lista[x][0], lista[x][1])
        
    elif option=="4":
        lista=[]
        
    elif option=="5":
        with open ("./data/registro_opciones.txt", "a") as registro:
            for x in range(len(lista)):
                print(lista[x][0], lista[x][1], file=registro, sep=",")
        salir=True      
        
    else:
        print("La opición ingresada no es correcta.")
