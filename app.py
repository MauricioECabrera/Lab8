from flask import Flask, render_template, request

app = Flask(__name__)

# FEATURE FLAG
VERSION_2_ACTIVA = True

@app.route("/", methods=["GET", "POST"])
def index():

    mensaje = ""

    if request.method == "POST":

        nombre = request.form["nombre"]

        if VERSION_2_ACTIVA:
            mensaje = f"Hello, {nombre}! - Version 2"
        else:
            mensaje = f"Hola, {nombre}! - Version 1"

    # Mostrar pantalla dependiendo de la flag
    if VERSION_2_ACTIVA:
        return render_template("v2.html", mensaje=mensaje)

    return render_template("v1.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)