from flask import Flask, render_template, request, redirect, make_response, url_for
from models import User, db, Stocks
import uuid, hashlib
from sqla_wrapper import SQLAlchemy
from cryptos import btc_price

app = Flask(__name__)
db.create_all()


@app.route("/")
def index():
    session_token = request.cookies.get("session_token")

    if session_token:
        user = db.query(User).filter_by(session_token=session_token).first()
    else:
        user = None

    return render_template("index.html", user=user)


@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    password = request.form.get("user-password")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # see if user already exists
    user = db.query(User).filter_by(email=email).first()

    if not user:
        # create a User object
        user = User(name=name, email=email, password=hashed_password)
        user.save()

    if hashed_password != user.password:
        return "Login failed. Please try again!"
    else:
        session_token = str(uuid.uuid4())
        user.session_token = session_token
        user.save()

        # save user's email into a cookie
        response = make_response(redirect(url_for('index')))
        response.set_cookie("session_token", session_token, httponly=True, samesite="Strict")

        return response


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
