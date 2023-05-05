# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:46:18 2023

@author: anaso
"""

from flask import Flask, render_template, request
import datetime
import csv
import random

from modulos.modulos import agregar_lista_archivo, guardar_3datos_en_archivo, frases_random_web, guardar_1dato_en_archivo

app = Flask(__name__)
lista = []
RUTA = "./data/"
ARCHIVO = RUTA + "historial_partidas.txt"
archivo = RUTA + "frases_de_peliculas.txt"

try:
    agregar_lista_archivo(ARCHIVO, lista)            
except FileNotFoundError:
    with open(ARCHIVO, "w") as archi:
        pass
        
with open (archivo, encoding="utf-8") as archivo:
  archi=csv.reader(archivo, delimiter=";")
  peliculas=list(archi)

matriz=[[0]*2 for x in range(len(peliculas))]
for x in range(len(peliculas)):
  matriz[x][0]=peliculas[x][0]
  matriz[x][1]=peliculas[x][1]

frases = frases_random_web(matriz)

usuario="anonimo"

@app.route("/", methods=['GET', 'POST'])
def raiz():
    global usuario
    if request.method == 'POST':
        usuario = request.form["nombre"]
        if usuario=="":
            usuario="anonimo"
    return render_template("main.html", usuario=usuario)

vueltas=0

@app.route("/trivia", methods=['GET', 'POST'])
def agregar():
    global cont
    global vueltas
    global puntaje_final
    if vueltas==6:
        vueltas=0
    valor=""
    x=random.randint(0,2)
    if request.method == 'POST':
        opcion = request.form["op"]
        if opcion == "correcta":
            valor="correcta"
            cont+=1
        else:
            valor="incorrecta"
            cont=cont
    if vueltas<6:
        vueltas+=1
        puntaje_final=cont
    if vueltas==6:
        puntaje_final=cont
        cont=0
    if vueltas == 1:
        frases1=frases[:3]
    elif vueltas==2:
        frases1=frases[3:6]
    elif vueltas==3:
        frases1=frases[6:9]
    elif vueltas==4:
        frases1=frases[9:12]
    elif vueltas==5:
        frases1=frases[12:]
    else:
        frases1=[]
    return render_template("trivia.html", frases=frases1, x=x, valor=valor, cont=cont, vueltas=vueltas, puntaje_final=puntaje_final)

@app.route("/historial", methods=['GET', 'POST'])
def historial():
    global usuario
    global puntaje_final
    global vueltas
    fecha=(str(datetime.datetime.now())[:19])
    if vueltas==5:
        datos={"nombre": usuario,
                "puntaje": puntaje_final,
                "fecha": fecha}
        lista.append(datos)
        guardar_3datos_en_archivo(ARCHIVO, datos)
        vueltas=0
    if len(lista) == 0:
        return render_template("historial.html", esta_vacia=True)
    else:
        return render_template("historial.html", esta_vacia=False, lista=lista)

if __name__ == "__main__":
    app.run(debug=True)

