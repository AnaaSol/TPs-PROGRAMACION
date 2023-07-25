import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk as nltk

def graficar_nube(texto):
    nltk.download('stopwords') #descarga las stopwords
    stopwords_es=nltk.corpus.stopwords.words('spanish') #se queda con las del español
    palabras_filtradas=[palabra for palabra in texto.split() if palabra.lower() not  in stopwords_es] #remueve stopwords
    # palabras_filtradas = []
    # for palabra in texto.split():
    #     if palabra.lower() not in sw_es:
    #         palabras_filtradas.append(palabra)
    texto_filtrado = ' '.join(palabras_filtradas)
    wd = WordCloud(width=800, height=400, background_color='white').generate(texto_filtrado) #se crea la nube
    fig, ax = plt.subplots(figsize=(8, 4)) #se crea la figura
    ax.imshow(wd, interpolation='bilinear')
    ax.set_axis_off() #se ocultan los ejes
    # plt.show()
    return wd

#funciona
#graficar_nube("Este es un serio problema, Mr. Jones. No sabemos nada aún de nuestro destino. Nuestro futuro ha sido puesto en pausa, y yo muero por vivir. Deseo que su mundo se reanude, para que devuelva a la vida al nuestro")

def graficar_torta(estados, depto):

    fig, axes=plt.subplots(figsize=(6,6), subplot_kw={"aspect":1})
    sizes = [50, 25, 20, 5] #sizes debería ser la cantidad de reclamos por estado = estados
    labels = ['Pendiente', 'En proceso', 'Resuelto', 'Inválido'] #el tp sólo pide los resueltos y en proceso
    axes.pie(sizes, labels=labels, autopct='%1.1f%%')
    axes.set_aspect('equal')
    axes.set_title(f"Total reclamos {depto}: {len(estados)}")
    plt.show()
    #plt.savefig(f"static/torta_{depto}.png")


