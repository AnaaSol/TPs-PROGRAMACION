import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk as nltk
import io
import base64

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
    plt.gca().set_facecolor('#f1f1f1')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    wd = base64.b64encode(buf.read()).decode('utf-8')
    return wd

#funciona
#graficar_nube("Este es un serio problema, Mr. Jones. No sabemos nada aún de nuestro destino. Nuestro futuro ha sido puesto en pausa, y yo muero por vivir. Deseo que su mundo se reanude, para que devuelva a la vida al nuestro")

def graficar_torta(estados, depto):
    cant=0
    for x in estados:
        cant+=x
    valores = estados #sizes debería ser la cantidad de reclamos por estado = estados
    etiquetas = ['Pendiente', 'En proceso', 'Resuelto', 'Inválido'] #el tp sólo pide los resueltos y en proceso
    colores = ['red', 'green', 'blue', 'orange']
    plt.figure(figsize=(8, 6))
    plt.pie(valores, labels=None, colors=colores, autopct=None)
    etiquetas_y_valores = [f'{etiqueta} - {valor}%' for etiqueta, valor in zip(etiquetas, valores)]
    plt.legend(etiquetas_y_valores, loc='best', bbox_to_anchor=(1, 0.5))
    plt.title(f"Total reclamos {depto}: {cant}")
    plt.gca().set_facecolor('#f1f1f1')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    torta = base64.b64encode(buf.read()).decode('utf-8')
    return torta
    #plt.savefig(f"static/torta_{depto}.png")




