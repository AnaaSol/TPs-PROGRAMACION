from modulos.classes import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def raiz():
    return render_template("main.html")

@app.route("/jefe", methods=['GET', 'POST'])
def jefe():
    return render_template("jefe.html")

@app.route("/usuario", methods=['GET', 'POST'])
def usuario():
    return render_template("usuario.html")

@app.route("/reclamo", methods=['GET', 'POST'])
def reclamo():
    return render_template("reclamo.html")