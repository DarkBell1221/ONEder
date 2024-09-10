from flask import Flask

from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hola, Mundo!</p>"

@app.route("/ONEder")
def ONEder():
    return render_template("ONEder.html")

@app.route("/ONEder/guardar", methods=["POST"])
def ONEderGuardar():

    matricula    =request.form["txtMatriculaFA"]
    nombreapellido    =request.form["txtNombreApellidoFA"]
    return f"matricula: {matricula} Nombre y Apellido: {nombreapellido}"
