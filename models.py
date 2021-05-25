from sqla_wrapper import SQLAlchemy

db = SQLAlchemy("sqlite:///db.sqlite")


class Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bezeichnung = db.Column(db.String, unique=False)
    stueckzahl = db.Column(db.Integer, unique=False)
    preis = db.Column(db.Float, unique=False)
    gesamtbetrag = db.Column(db.Float, unique=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    session_token = db.Column(db.String)
    secret_number = db.Column(db.Integer, unique=False)