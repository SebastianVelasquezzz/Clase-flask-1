from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


@app.route("/recursos")
def recursos():
   
    recursos = [
        "Entorno virtual",
        "Rutas en Flask",
        "Plantillas HTML",
        "Variables con Jinja"
    ]
    
    return render_template("recursos.html", recursos=recursos)

if __name__ == "__main__":
    app.run(debug=True)






