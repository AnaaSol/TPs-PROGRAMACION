import funciones_acciones
import matplotlib.pyplot as plt

matriz=funciones_acciones.abrir_archivos("./docs/google.csv")

trimestre=[]
for x in range(len(matriz)):
    fecha=matriz[x][0].split("/")
    mes=int(fecha[1])
    if (mes>=1) and (mes<=3):
        trimestre.append(matriz[x])
    
minimo_trimestral=funciones_acciones.max_min(trimestre, 1)[0]
maximo_trimestral=funciones_acciones.max_min(trimestre, 1)[1]
variacion_tri=funciones_acciones.variacion_porcentual(minimo_trimestral, maximo_trimestral)

min_anual=funciones_acciones.max_min(matriz, 1)[1]
fin_anual=matriz[-1][1]
repunte_anual=funciones_acciones.variacion_porcentual(min_anual, fin_anual)

print(variacion_tri)
print(maximo_trimestral)
print(minimo_trimestral)

"""Rta.b.d.: La variación porcentual calculada en los puntos a y c no se 
corresponden con el gráfico de la derecha porque este considera como punto de
referencia el valor del día 1"""

max_anual=funciones_acciones.max_min(matriz, 1)[0]

x=[]
y=[]
for i in range(len(matriz)):
    x.append(i)
    valor=(matriz[i][1]-min_anual)/(max_anual-min_anual)
    y.append(valor)

matriz1=funciones_acciones.abrir_archivos("./docs/nike.csv")
max_anual_nike=funciones_acciones.max_min(matriz1, 1)[0]
min_anual_nike=funciones_acciones.max_min(matriz1, 1)[1]

x1=[]
y1=[]    
for i in range(len(matriz1)):
    x1.append(i)
    valor1=(matriz1[i][1]-min_anual_nike)/(max_anual_nike-min_anual_nike)
    y1.append(valor1)   

a=[]
b=[]
inicio=matriz[0][1]
for i in range(len(matriz)):
    a.append(i)
    nuevo=((matriz[i][1]-inicio)/inicio)*100
    b.append(nuevo)

a1=[]
b1=[]
inicio1=matriz1[0][1]
for i in range(len(matriz1)):
    a1.append(i)
    nuevo1=((matriz1[i][1]-inicio1)/inicio1)*100
    b1.append(nuevo1)

#dos filas, una columna, la primera
plt.subplot(2, 1, 1)
#la función plot une los elementos de las listas x e y uno a uno para obtener las coordenadas de los puntos con los que grafica la curva.
plt.plot(x,y, label="Google", color="blue")
plt.plot(x1, y1, label="Nike", color="orange")
plt.legend()
plt.grid()

#dos filas, una columna, la segunda
plt.subplot(2, 1, 2)
plt.plot(a, b, label="Google", color="blue")
plt.plot(a1, b1, label="Nike", color="orange")

plt.legend()
plt.grid()
plt.show()
