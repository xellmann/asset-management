from flask import Flask, render_template, request, redirect
from sqla_wrapper import SQLAlchemy
from cryptos import btc_price

app = Flask(__name__)
db = SQLAlchemy("sqlite:///db.sqlite")


class Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bezeichnung = db.Column(db.String, unique=False)
    stueckzahl = db.Column(db.Integer, unique=False)
    preis = db.Column(db.Float, unique=False)
    gesamtbetrag = db.Column(db.Float, unique=False)


db.create_all()

@app.route("/")
def index():
    stocks = db.query(Stocks).all()
    return render_template("index.html", stocks=stocks)

@app.route("/bookings")
def bookings():
    stocks = db.query(Stocks).all()
    return render_template("bookings.html", stocks=stocks)

@app.route("/add-message", methods=["POST"])
def add_message():
    bezeichnung = request.form.get("bezeichnung")
    stueckzahl = int(request.form.get("stueckzahl"))
    preis = float(request.form.get("preis"))
    gesamtbetrag = preis*stueckzahl
    asset = Stocks(bezeichnung=bezeichnung, stueckzahl=stueckzahl, preis=preis, gesamtbetrag=gesamtbetrag)
    asset.save()

    return redirect("/bookings")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
