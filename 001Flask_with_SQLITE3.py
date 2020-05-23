from cs50 import SQL
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

db = SQL("sqlite:///lecture.db")

@app.route("/")
def index():
    rows = db.execute("SELECT * FROM registrants")
    return render_template("index.html", rows=rows)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("name")
        if not name:
            return render_template("apology.html", message="You must provide a name.")
        email = request.form.get("email")
        if not email:
            return render_template("apology.html", message="You must provide a email.")
        db.execute("INSERT INTO registrants (name, email) VALUES (:name, :email)", name=name, email=email)
        return redirect("/")

   '''
   it containes another file call lacture.db
    Create table registrants(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ##itableregistrantsregistrantsCREATE TABLE 'registrants' (
    'id' INTEGER PRIMARY KEY,
    'name' VARCHAR(255),
    'email' VARCHAR(255)
)
and a folder call templates which containg index.html,layout.html,register.html,apology.html
   ''' 
