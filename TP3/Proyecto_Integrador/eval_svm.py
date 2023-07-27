# import pickle as p
# from modules.clasificador import Clasificador
# from modules.preprocesamiento import TextVectorizer

# #cls =  Clasificador()

# # import os
# # ruta_absoluta = os.path.abspath('data\clasificador_svm.pkl')
# # print(ruta_absoluta)

# with open('data\clasificador_svm.pkl', "rb") as tuqui:
#   cls  = p.load(tuqui)

# # cls = pd.read_pickle('data/clasificador_svm.pkl')

# text= ["no funciona el campus virtual "]
# print(cls.clasificar(text))


import matplotlib.pyplot as plt
fig=plt.figure(figsize=(5, 5))
ax= plt.subplot()

x = [10, 20, 30]
y1 = [20, 40, 10]
y2 =[40, 10, 30]

plt.plot(x, [20, 40, 10])
plt.plot(x, [40, 10, 30])


plt.text(15, 15, "$(x', y')$")
plt.grid()
plt.show()
