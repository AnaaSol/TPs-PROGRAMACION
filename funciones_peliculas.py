# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 07:26:49 2023

@author: anaso
"""

import random
import csv


with open ("frases_de_peliculas.txt") as archivo:
  archi=csv.reader(archivo, delimiter=";")
  peliculas=list(archi)

matriz=[[0]*2 for x in range(len(peliculas))]
for x in range(len(peliculas)):
  matriz[x][0]=peliculas[x][0]
  matriz[x][1]=peliculas[x][1]

def frases_random(matrix):
  "Devuelve una matriz con tres listas de frases random y sus respectivas películas."
  matriz=[]
  list=random.sample(range(len(matrix)),3)
  for number in list:
    phrase=[matrix[number][0], matrix[number][1]]
    matriz.append(phrase)
  return matriz
