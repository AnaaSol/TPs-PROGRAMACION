# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:47:30 2023

@author: anaso
"""
import csv
import random

def agregar_lista_archivo (nombre_archivo, lista):
    with open (nombre_archivo) as file:
            file=csv.reader(file, delimiter=",")
            file=list(file)
            for x in file:
                datos={"nombre":x[0],
                       "puntaje":x[1],
                       "fecha":x[2]}
                lista.append(datos)


def guardar_3datos_en_archivo (nombre_archivo, datos):
    with open (nombre_archivo, "a", encoding="utf-8") as archi:
            print(datos["nombre"], datos["puntaje"], datos["fecha"], file=archi, sep=",")

def frases_random(matrix):
  "Devuelve una matriz con 3 listas de frases random y sus respectivas películas."
  matriz=[]
  list=random.sample(range(len(matrix)),3)
  for number in list:
    phrase=[matrix[number][0], matrix[number][1]]
    matriz.append(phrase)
  return matriz

def frases_random_web(matrix):
  "Devuelve una matriz con 15 listas de frases random y sus respectivas películas."
  matriz=[]
  list=random.sample(range(len(matrix)),15)
  for number in list:
    phrase=[matrix[number][0], matrix[number][1]]
    matriz.append(phrase)
  return matriz
