from flask import Flask, render_template, request

app = Flask(__name__)

productos = {}

@app.route("/agregarproducto")
def agregarproducto():
	nombre = request.args.get("nombre")
	precio = request.args.get("precio")
	cantidad = request.args.get("cantidad")

@app.route('/')
def index():
	return 'Hello, Flask!'

if __name__ == '__main__':
	app.run(debug=True)