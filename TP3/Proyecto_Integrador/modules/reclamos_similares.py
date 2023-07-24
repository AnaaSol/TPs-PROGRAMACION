#from usuario import *
import nltk as nltk
import collections
import operator

def reclamos_similares (reclamos_same_depto, texto_objetivo): #reclamos_same_depto es una lista de tuplas con la descripcion de los reclamos y su ID (descrip, ID)
    
    cont=0
    similares=[]
    lista_objetivo=[] #lista de palabras del texto objetivo en orden de su frecuencia
    lista_reclamo=[] #lista de palabras de los textos de mismo depto en orden de su frecuencia
    lista_comparacion=[] #lista de lista_reclamos
    
    #filtro de palabras
    nltk.download('stopwords')
    stopwords_es=nltk.corpus.stopwords.words('spanish')
    palabras_filtradas_objetivo=[palabra for palabra in texto_objetivo.split() if palabra.lower() not  in stopwords_es]
    texto_filtrado_objetivo = ' '.join(palabras_filtradas_objetivo) #¿no es al cuete si después las separás de vuelta?
    counter1 = collections.Counter(texto_filtrado_objetivo.split()) #diccionario que mapea cada elemento con su frecuencia
    for palabra, cont in counter1.most_common(): #el método most_common retorna una lista de parejas ordenada en función del orden de apariciones, de mayor a menor
        lista_objetivo.append(palabra) #uso solo la palabra, descartando el numero de veces que se repite (pero manteniendo el orden)
    
    #mismo proceso para textos same depto
    for x in range(len(reclamos_same_depto)):
        palabras_filtradas=[palabra for palabra in reclamos_same_depto[x][0].split() if palabra.lower() not  in stopwords_es]
        texto_filtrado = ' '.join(palabras_filtradas)
        counter = collections.Counter(texto_filtrado.split())
        for palabra, cont in counter.most_common(): #el método most_comons retorna una lista de parejas ordenada en función del orden de apariciones, de mayor a menor
            lista_reclamo.append(palabra) #uso solo la palabra, descartando el numero de veces que se repite (pero manteniendo el orden)
        tupla=(lista_reclamo, reclamos_same_depto[x][1]) #tupla con la lista de palabras y el ID del reclamo
        lista_comparacion.append(tupla)
        lista_reclamo=[]

    #comparar las palabras significativas que aparecen y compararlas con el texto objetivo
    for i in lista_comparacion:
        cont=0
        for x in lista_objetivo:
            if x in i[0]:
                cont+=1
                #print(cont)
            #print (x, i[0])
        prom=(cont/len(lista_objetivo))*100 #promedio respecto al texto objetivo
        prom2=(cont/len(i[0])*100) #promedio respecto al posible reclamos similar
        if prom>=70 and prom2>=65:
            similares.append([i[1], prom])
    similares.sort(key=operator.itemgetter(1), reverse=True) #los ordena de mayor a menor similitud
    lista_IDs=[]
    for j in range(len(similares)):
        lista_IDs.append(similares[j][0])
    return lista_IDs #devuelve una lista con los ID del/los reclamo/s similar/es 

if __name__== "__main__": 
    print(reclamos_similares([("hola prueba reclamos similares encontrados", 1), ("hola prueba", 2), ("hola prueba completa reclamos similares encontrados", 3)], "hola prueba completa reclamos similares encontrados"))
    # lista_de_tuplas=[("tuqui", 37, "alapucha", 999), (1, 2), (1,3), (8, "boe ya basta")]
    # print(lista_de_tuplas[0][0])
    # print(lista_de_tuplas[3][1])