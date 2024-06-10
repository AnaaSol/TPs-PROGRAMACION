#flask
from flask import Flask, render_template, request, redirect, url_for, session

#clasificador
from modules.clasificador import Clasificador 
from modules.preprocesamiento import TextVectorizer

#clases
from modules.gestores import Gestor_de_base_de_datos, Gestor_de_reclamos
from modules.usuario import Usuario
from modules.reclamo import Reclamo

#clases modelo (tablas de db)
from modules.databases import *

#funciones
from modules.funciones import graficar_nube, graficar_torta
from modules.reclamos_similares import reclamos_similares

#otros módulos
import datetime
import io
import base64
from functools import wraps
from modules.config import app, db

#excepciones
from sqlalchemy.orm.exc import NoResultFound 

GestorDB=Gestor_de_base_de_datos()
GestorR=Gestor_de_reclamos('./data/clasificador_svm.pkl') 

with app.app_context():
    db.create_all()
    
@app.route("/", methods=['GET', 'POST'])
def raiz():  
    condicion=""
    if request.method == 'POST':
        u=request.form["usuario"]
        c=request.form["contraseña"] 
        if not u or not c:
            condicion="Complete ambos campos"
        else:
            try:
                actual_password=GestorDB.get_dato_user(u, "password") #contraseña correcta del usuario
            # except Exception as e: #either el usuario no existe o el dato es inválido (el dato es válido, está chequeado)
            #     condicion=str(e)
            except:
                condicion="El usuario no existe"
            else: #bloque que se ejecuta si en try no hubo excepción
                if actual_password==c: #compara la contraseña correcta con la ingresada
                    type=GestorDB.get_dato_user(u, "depto") 
                    if not type: #es decir, type=None
                        return redirect(url_for('usuario', user=u)) 
                    else:
                        return redirect(url_for('jefe', depto=type))
                else:
                    condicion="La contraseña es incorrecta"

    return render_template("main.html", condicion=condicion)

@app.route("/sing_up", methods=['GET', 'POST'])
def new_user():
    condicion=""
    if request.method == 'POST':
        name=request.form["name"]
        apellido=request.form["surname"]
        mail=request.form["email"]
        user_name=request.form["username"]
        cloister=request.form["cloister"]
        contraseña=request.form["password"]
        rep_contraseña=request.form["password_again"]

        if not name or not apellido or not mail or not user_name or not cloister or not contraseña or not rep_contraseña:
            condicion="Faltan ingresar datos. Por favor complete todos los campos"

        elif GestorDB.chequear_disponibilidad("email", mail)=="Email/usuario ocupado":
            condicion="Ya existe una cuenta con ese email"

        elif GestorDB.chequear_disponibilidad("username", user_name)=="Email/usuario ocupado":
            condicion="Ya existe una cuenta con ese nombre de usuario"

        elif contraseña!=rep_contraseña:
            condicion="Las contraseñas ingresadas no coinciden"

        else:
            #en lugar de crear el objeto directamento lo guardamos en la bd
            datos_user=[name, apellido, mail, user_name, contraseña, cloister, "", ""]
            GestorDB.guardar_nuevo_objeto("usuario", datos_user)
            return redirect(url_for('raiz'))
            
    return render_template("sing_up.html", condicion=condicion)

@app.route("/jefe/<depto>", methods=['GET', 'POST'])
def jefe(depto):
    depto=depto.capitalize()
    if request.method == 'POST':
        direction=request.form["button_value"] #it's either "Manejar reclamos" o "Analítica" (o "Panel general" si el jefe es el de secretaría técnica)
        if direction=="Manejar reclamos":
            return redirect(url_for('manejar', depto=depto))
        elif direction=="Analítica":
            return redirect(url_for('analitica', depto=depto)) 
        elif direction=="Panel general":
            return redirect(url_for('panel_general', depto=depto))
    reclamos_depto=GestorDB.get_reclamos_by_filtro("departamento", depto.lower()) #obtiene la data de los reclamos del depto
    if len(reclamos_depto)!=0: #es decir, hay reclamos para el depto
        descripciones=[reclamo[1] for reclamo in reclamos_depto] #se queda con las descripciones
        texto = ' '.join(descripciones) #forma un texto
        cantidades=GestorDB.contar_cantidad(depto.lower()) #obtiene la cantidad de reclamos por estado del depto
        nube_cod = graficar_nube(texto) #Obtiene la nube de palabras
        torta_cod = graficar_torta(cantidades, depto)  #Obtiene el gráfico de torta
        return render_template("jefe.html", depto=depto, nube_cod=nube_cod, torta_cod=torta_cod, reclamos=reclamos_depto)
    else:
        return render_template("jefe.html", depto=depto, reclamos=reclamos_depto)
    
@app.route("/panel_general/<depto>", methods=['GET', 'POST'])
def panel_general(depto):
    reclamos_generales_data=GestorDB.get_reclamos_by_filtro()
    reclamos_generales=GestorR.cargar_de_db(reclamos_generales_data)
    cant=len(reclamos_generales)
    return render_template("panel_general.html", depto=depto, reclamos=reclamos_generales, cant=cant)

@app.route("/manejar/<depto>", methods=['GET', 'POST'])
def manejar(depto):

    if request.method == 'POST':
        if "action" in request.form:
            ID=request.form["ID"]
            print("este es el ID", ID)
            action=request.form["action"]
            if action=="estado":
                print(action)
                nuevo_estado=request.form["nuevo_estado"]
                datos=GestorDB.get_reclamos_by_filtro("ID", ID)[0]
                ID_usuario_creador=datos[3]
                if datos[7]=="": #es decir, no hay adherentes
                    ID_usuarios_interesados=[ID_usuario_creador]
                else:
                    ID_usuarios_interesados=[ID_usuario_creador]
                    for adh in datos[7].split(" "):
                        ID_usuarios_interesados.append(int(adh))

                for ID_user in ID_usuarios_interesados:
                    GestorDB.modificar_dato("actualizacion", "actualizacion", "usuario", ID_user)
                GestorDB.modificar_dato("estado", nuevo_estado, "reclamo", ID)
            elif action=="departamento":
                nuevo_depto=request.form["nuevo_depto"]
                GestorDB.modificar_dato("depto", nuevo_depto, "reclamo", ID)

    reclamos_de_depto_data=GestorDB.get_reclamos_by_filtro("departamento", depto.lower()) #se obtienen los datos de los reclamos del depto de bd
    reclamos=GestorR.cargar_de_db(reclamos_de_depto_data) #lista de objetos Reclamo
    length=len(reclamos)

    return render_template("reclamo_depto.html", depto=depto, reclamos=reclamos, len=length)

@app.route("/analitica/<depto>", methods=['GET', 'POST'])
def analitica(depto):

    reclamos_depto=GestorDB.get_reclamos_by_filtro("departamento", depto.lower()) #obtiene la data de los reclamos del depto
    if len(reclamos_depto)!=0:
        descripciones=[reclamo[1] for reclamo in reclamos_depto] #se queda con las descripciones
        texto = ' '.join(descripciones) #forma un texto
        cantidades=GestorDB.contar_cantidad(depto.lower()) #obtiene la cantidad de reclamos por estado del depto
        nube_cod = graficar_nube(texto) #Obtiene la nube de palabras
        torta_cod = graficar_torta(cantidades, depto)  #Obtiene el gráfico de torta
        return render_template("analitica.html", depto=depto, nube_cod=nube_cod, torta_cod=torta_cod)
    else:
        return render_template("analitica.html", depto=depto)

@app.route("/usuario/<user>", methods=['GET', 'POST'])
def usuario(user):
    session['username'] = user
    return render_template("usuario.html", user=user)

@app.route("/reclamo", methods=['GET', 'POST'])
def crear():

    user=session.get('username')
    ID=GestorDB.get_dato_user(user, "ID")

    if request.method == "POST":

        if 'action' in request.form:

            action = request.form['action']

            if action == 'volver_a_usuario':
                return redirect(url_for('usuario', user=user, action=action))
            elif action == 'crear':
                #creación del objeto Usuario
                usser=Usuario(GestorDB.get_dato_user(user, "ID"), GestorDB.get_dato_user(user, "name"), GestorDB.get_dato_user(user, "surname"), user, GestorDB.get_dato_user(user, "email"), GestorDB.get_dato_user(user, "password"), GestorDB.get_dato_user(user, "claustro"))

                #creación del formulario para el reclamo
                texto=request.form["description"]
                formulario=usser.generar_datos_reclamo(texto)
                #imagen
                imagen=request.files["image"]
                if imagen: #es decir, imagen no es None
                    imagen_data = imagen.read()
                    formulario.append(imagen_data)
                #se añade un ID provisorio para poder crear el reclamo
                formulario.insert(0, 1) #formulario[0]=1
                #se crea el reclamo
                reclamo=GestorR.crear_reclamo(formulario)
                #se clasifica
                GestorR.clasificar_reclamo(reclamo)

                posibles=GestorDB.get_reclamos_by_filtro("departamento", reclamo.get_departamento) #obtiene los datos de los reclamos con el mismo departamento que el reclamo objetivo
                if len(posibles)!=0:
                    posibles_data=[] #guarda tuplas con la descripción de los reclamos y su ID
                    for x in range(len(posibles)): 
                        posibles_data.append((posibles[x][1], posibles[x][0])) #se queda con la descripción y el ID
                    similares=reclamos_similares(posibles_data, texto) #lista con los ID de los reclamos similares
                else:
                    similares=[]

                if len(similares)==0: #es decir, no se encontraron reclamos del mismo depto o que además sean similares
                    data=[reclamo.get_descripcion, reclamo.get_estado, reclamo.get_departamento, reclamo.get_fecha, reclamo.get_ID_usuario]
                    if reclamo.get_imagen: #es decir, imagen no es None
                        data.append(reclamo.get_imagen)
                        #print(data)
                    GestorDB.guardar_nuevo_objeto("reclamo", data)
                    return render_template("reclamo.html", reclamos_similares="no hay reclamos similares")
                else:
                    lista_similares=[]
                    for i in range(len(similares)):
                        reclamo_data=GestorDB.get_reclamos_by_filtro("ID", similares[i]) #seguro existen los reclamos con ese ID porque vienen de una consulta a la bd
                        #print(reclamo_data)
                        reclamo=GestorR.cargar_de_db(reclamo_data)
                        # print(reclamo.get_descripcion)
                        lista_similares.append(reclamo[0])
                    return render_template("reclamo.html", lista_similares=lista_similares, ID=ID, formulario=formulario)
                
            elif action=='adherir':
                ID_user=str(GestorDB.get_dato_user(user, "ID"))
                ID_reclamo=int(request.form["ID_reclamo"])
                datos_actuales_reclamo=GestorDB.get_reclamos_by_filtro("ID", ID_reclamo) #obtiene los datos del reclamo
                adherentes_actuales=datos_actuales_reclamo[0][7] #se queda con los adherentes 
                adheridos_actuales=GestorDB.get_dato_user(user, "reclamos_adheridos") #obtiene los reclamos adheridos del usuario
                if adherentes_actuales=="":
                    adherentes_actualizados=ID_user
                else:
                    adherentes_actualizados=adherentes_actuales+" "+ID_user

                if adheridos_actuales=="":
                    adheridos_actualizados=adheridos_actuales
                else:
                    adheridos_actualizados=adherentes_actuales+" "+str(ID_reclamo) 

                GestorDB.modificar_dato("adherentes", adherentes_actualizados, "reclamo", ID_reclamo)
                GestorDB.modificar_dato("reclamos_adheridos", adheridos_actualizados, "usuario", int(ID_user))
                return render_template("reclamo.html", reclamos_similares="adhirió", user=user)
            
            elif action=='crear_igualmente':
                formulario=[]
                formulario.append(request.form["crear_reclamo_ID"])
                formulario.append(request.form["crear_reclamo_descrip"])
                formulario.append(request.form["crear_reclamo_fecha"])
                formulario.append(request.form["crear_reclamo_ID_usuario"])
                for x in range(50):
                    print(formulario)
                #se crea el reclamo
                rcl=GestorR.crear_reclamo(formulario)
                #se clasifica
                GestorR.clasificar_reclamo(rcl)
                data=[rcl.get_descripcion, rcl.get_estado, rcl.get_departamento, rcl.get_fecha, rcl.get_ID_usuario]
                if rcl.get_imagen: #es decir, imagen no es None
                    data.append(rcl.get_imagen)
                    #print(data)
                GestorDB.guardar_nuevo_objeto("reclamo", data)
                return render_template("reclamo.html", reclamos_similares="no hay reclamos similares")
    else:
        return render_template("reclamo.html", reclamos_similares="todavia no buscados", user=user)

@app.route("/reclamos_pendientes", methods=['GET', 'POST'])
def pendientes():

    reclamos_pendientes=[]
    user=session.get('username')
    ID_user=str(GestorDB.get_dato_user(user, "ID"))

    if request.method== 'POST': #POST de adhesión a det reclamo
        try:
            ID_reclamo=int(request.form["ID_reclamo"])
            adherentes_actuales=GestorDB.get_reclamos_by_filtro("ID", ID_reclamo) #obtiene los datos del reclamo
            adherentes_actuales=adherentes_actuales[0][7] #se queda con los adherentes 
            adheridos_actuales=GestorDB.get_dato_user(user, "reclamos_adheridos") #obtiene los reclamos a los que adhirió el usuario
            # print("actuales=", adheridos_actuales)
            if adherentes_actuales=="":
                adherentes_actualizados=ID_user
            else:
                adherentes_actualizados=adherentes_actuales+" "+ID_user

            if adheridos_actuales=="":
                    adheridos_actualizados=str(ID_reclamo)
            else:
                    adheridos_actualizados=adherentes_actuales+" "+str(ID_reclamo) 
            # print("actualizados=", adheridos_actualizados)
            GestorDB.modificar_dato("adherentes", adherentes_actualizados, "reclamo", ID_reclamo)
            GestorDB.modificar_dato("reclamos_adheridos", adheridos_actualizados, "usuario", int(ID_user))

        except: #es la otra solicitud POST (filtro de reclamos)
            pass

    reclamos_pendientes_data = GestorDB.get_reclamos_by_filtro("estado", "pendiente")
    # print(reclamos_pendientes_data)
    cant=len(reclamos_pendientes_data)
    # print(cant)

    filtro="todos"
    if request.method== 'POST':
        try:
            filtro=request.form["filtro"]
        except:
            pass

    if cant!=0:
        reclamos_pendientes_sin_filtrar=GestorR.cargar_de_db(reclamos_pendientes_data)
        if filtro=="todos":
            reclamos_pendientes=reclamos_pendientes_sin_filtrar
        else:
            reclamos_pendientes=GestorR.filtrar_por_depto(reclamos_pendientes_sin_filtrar, filtro)

    ID_user=int(ID_user)
    return render_template("reclamos_pendientes.html", reclamos_pendientes=reclamos_pendientes, cant=cant, user=user, ID_user=ID_user)

@app.route("/reclamos_usuario", methods=['GET', 'POST'])
def reclamos_user():

    user=session.get('username')
    ID_user=GestorDB.get_dato_user(user, "ID")
    reclamos=[]
    data_reclamos_creados=GestorDB.get_reclamos_by_filtro("usuario", ID_user) #obtiene la data de los reclamos creados por user
    ID_reclamos_adheridos=GestorDB.get_dato_user(user, "reclamos_adheridos")

    if ID_reclamos_adheridos=="":
        pass
    else: 
        IDs=[ID for ID in ID_reclamos_adheridos.split(" ")] #obtiene los ID de los reclamos adheridos por user
        adheridos=[]
        for ID in IDs:
            data=GestorDB.get_reclamos_by_filtro("ID", int(ID))
            claim=GestorR.cargar_de_db(data)[0]
            # print(claim)
            adheridos.append(claim)
        for r in adheridos:
            reclamos.append(r)
    
    if len(data_reclamos_creados)!=0:
        creados=GestorR.cargar_de_db(data_reclamos_creados)
        for r in creados:
            reclamos.append(r)

    cant=len(reclamos)

    if GestorDB.get_dato_user(user, "actualizacion")=="actualizacion":
        print(GestorDB.get_dato_user(user, "actualizacion"))
        notificacion="¡Novedades! Hubieron cambios a sus reclamos"
        GestorDB.modificar_dato("actualizacion", "ninguna", "usuario", ID_user)
    else:
        print(GestorDB.get_dato_user(user, "actualizacion"))
        notificacion="nada"
    
    return render_template("reclamos_usuario.html",  reclamos=reclamos, user=user, cant=cant, notificacion=notificacion)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')