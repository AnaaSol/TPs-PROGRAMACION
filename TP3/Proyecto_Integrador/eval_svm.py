import pickle as p
from modules.clasificador import Clasificador
from modules.preprocesamiento import TextVectorizer

#cls =  Clasificador()

# import os
# ruta_absoluta = os.path.abspath('data\clasificador_svm.pkl')
# print(ruta_absoluta)

with open('data\clasificador_svm.pkl', "rb") as tuqui:
  cls  = p.load(tuqui)

# cls = pd.read_pickle('data/clasificador_svm.pkl')

text= ["no funciona el campus virtual "]
print(cls.clasificar(text))
