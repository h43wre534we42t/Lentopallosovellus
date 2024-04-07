from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute(text("SELECT name, id FROM courts"))
    courts = result.fetchall()
    return render_template("index.html", courts=courts)

@app.route("/addcourt")
def addcourt():
    return render_template("addcourt.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form['name']
    address = request.form['address']
    sql = text("INSERT INTO courts (name, address) VALUES (:name, :address)")
    db.session.execute(sql, {"name":name, "address":address})
    db.session.commit()
    return redirect("/")
    
@app.route("/court/<int:court_id>")
def court(court_id):
    sql = text("SELECT name, address FROM courts WHERE id = :id")
    court = db.session.execute(sql, {"id":court_id}).fetchone()
    sql = text("SELECT * FROM reserved WHERE court_id = :court_id")
    reservations = db.session.execute(sql, {"court_id":court_id}).fetchall()
    return render_template("court.html", court=court, reservations=reservations)