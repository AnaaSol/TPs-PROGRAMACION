import pickle
from modulos.ClasificadorSk.clasificadorsk.modules.clasificador import Clasificador
from modulos.ClasificadorSk.clasificadorsk.modules.preprocesamiento import TextVectorizer

import sys
sys.path.append('modulos\ClasificadorSk\clasificadorsk\modules')

#cls =  Clasificador()

with open('D:\\usuarios\\alumno\\escritorio\\PROGRAMACIÓN\\TPs-PROGRAMACION\\TP3\\Proyecto_Integrador\\modulos\\ClasificadorSk\\clasificadorsk\\data\\clasificador_svm.pkl', 'rb') as archivo:
  print(archivo)
  cls  = pickle.load(archivo)

text= ["no funciona el campus virtual "]
print(cls.clasificar(text))