from app import app
from db import db
from flask import redirect, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv

app.secret_key = getenv("SECRET_KEY")

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
    return render_template("reserve.html", court_id=court_id)

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

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    sql = text("SELECT * FROM users WHERE username = :username AND password = :password")
    is_user = db.session.execute(sql, {"username":username, "password":password}).fetchone()

    if is_user:
        session["username"] = username
    else:
        flash("Invalid username or password")

    return redirect("/")

@app.route("/registration")
def registration():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    existing_user = db.session.execute(text("SELECT * FROM users WHERE username = :username"), {"username": username}).fetchone()

    if existing_user:
        flash("Username already exists. Please choose a different username.")
        return redirect("/registration")
    else:

        sql = text("INSERT INTO users (username, password, is_admin) VALUES (:username, :password, false)")
        
        db.session.execute(sql, {"username": username, "password": password})
        db.session.commit()

        return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


# add groups