from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def index():
	return render_template("index.html")


@app.route("/tramites/")
def tramites():
	return render_template("tramites.html")


@app.route("/informacion/")
def informacion():
	return render_template("informacion.html")


@app.route("/contacto/")
def contacto():
	return render_template("contacto.html")
