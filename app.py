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
    return render_template("court.html", court=court, reservations=reservations, court_id=court_id)

@app.route("/reserve/<int:court_id>")
def reserve(court_id):
    return render_template("reserve", {"court_id":court_id})

@app.route("/reservesend/<int:court_id>", methods=["POST"])
def reservesend(court_id):
    res_date = request.form['res_date']
    res_start = request.form['res_start']
    res_end = request.form['res_end']
    reservee = request.form['reservee']
    sql = text("INSERT INTO reserved (res_date, res_start, res_end, court_id, reservee) VALUES (:res_date, :res_start, :res_end, :court_id, :reservee)")
    db.session.execute(sql, {"res_date":res_date, "res_start":res_start, "res_end":res_end, "reservee":reservee, "court_id":court_id})
    db.session.commit()
    return redirect("/")