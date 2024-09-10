from flask import Flask

from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hola, Mundo!</p>"

@app.route("/ONEder")
def alumnos():
    return render_template("ONEder.html")

@app.route("/ONDER/guardar", methods=["POST"])
def alumnosGuardar():

    matricula    =request.form["txtMatriculaFA"]
    nombreapellido    =request.form["txtNombreApellidoFA"]
    return f"matricula: {matricula} Nombre y Apellido: {nombreapellido}"
