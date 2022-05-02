from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/user", methods=["POST"])
def login():
	firstname = request.form.get("nombre")
	lastname = request.form.get("apellido")
	ocupation = request.form.get("ocupacion")
	date = request.form.get("fecha")
	email = request.form.get("correo")
	phone = request.form.get("numero")
	password = request.form.get("constraseña")
	
	return render_template(
		"session.html",
		lastname=lastname,
		firstname=firstname,
		ocupation=ocupation,
		date=date,
		email=email,
		phone=phone,
		password=password,
		)


@app.route("/<string:name>")
def session(name):
	return render_template(
		"session.html",
		name=name,
		)

@app.route("/users")
def names():
	# Query a DB for users.
	name_list = ["Jose", "Pedro", "Maria"]
	return render_template(
		"list.html",
		names=name_list,
	)
