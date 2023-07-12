from usuario import *
import nltk as nltk
import collections

def reclamos_similares (reclamos_same_depto, texto_objetivo): #reclamos_same_depto es una lista con la descripcion de los reclamos
    #eliminar conectores/prefijos etc
    cont=0
    similares=[]
    lista_objetivo=[]
    lista_reclamo=[]
    lista_comparacion=[]
    nltk.download('stopwords')
    stopwords_es=nltk.corpus.stopwords.words('spanish')
    palabras_filtradas_objetivo=[palabra for palabra in texto_objetivo.split() if palabra.lower() not  in stopwords_es]
    texto_filtrado_objetivo = ' '.join(palabras_filtradas_objetivo)
    counter1 = collections.Counter(texto_filtrado_objetivo.split())
    for palabra, cont in counter1.most_common(): #el método most_comons retorna una lista de parejas ordenada en función del orden de apariciones, de mayor a menor
        lista_objetivo.append(palabra) #uso solo la palabra, descartando el numero de veces que se repite (pero manteniendo el orden)
    #lista_objetivo=list(palabras_filtradas_objetivo)
    for x in range(len(reclamos_same_depto)):
        palabras_filtradas=[palabra for palabra in reclamos_same_depto[x].split() if palabra.lower() not  in stopwords_es]
        texto_filtrado = ' '.join(palabras_filtradas)
        counter = collections.Counter(texto_filtrado.split())
        for palabra, cont in counter.most_common(): #el método most_comons retorna una lista de parejas ordenada en función del orden de apariciones, de mayor a menor
            lista_reclamo.append(palabra) #uso solo la palabra, descartando el numero de veces que se repite (pero manteniendo el orden)
        lista_comparacion.append(lista_reclamo)
        lista_reclamo=[]
    for i in lista_comparacion:
        for x in lista_objetivo:
            if x in i:
                cont+=1
            print (x, i)
        prom=(cont/len(i))*100
        if prom>=70:
            indice=lista_comparacion.index(i)
            similares.append(reclamos_same_depto[indice])
        elif prom==100:
            pass #agregar control
        #comparar las palabras significativas que aparecen y compararlas con el texto objetivo
    return similares #devuelve la descripcion del/los reclamo/s similar/es

print(reclamos_similares(["esto es es una prueba una prueba prueba para evaluar el correcto funcionamiento de reclamos para evaluar reclamos similares"], "prueba evaluar el correcto funcionamiento")) #podriamos agregar un flitro para sinonimos
