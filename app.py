from flask import Flask
app = Flask(__name__)

# Ruta bienvenida
@app.route("/")
def hello_world():
    return "¡Bienvenidos a mi aplicación Flask!"

#Ruta /about
@app.route("/uic")
def uic_function():
    return "Acerca de esta página"

#Ruta /contact
@app.route("/uic2")
def uic_function2():
    return "Contáctanos en flask@example.com"

#Ruta /contact
@app.route("/uic3")
def uic_function2():
    return "Probando con Git"

#Ruta /hobbies
# @app.contact("/")
# def hello_world():
#     return "Mis hobbies son programar y leer"