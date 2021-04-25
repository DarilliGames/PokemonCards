import os
from flask import Flask, render_template, redirect, request, session
from flask_pymongo import PyMongo
import gspread
from google.oauth2.service_account import Credentials
import json

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

if os.path.exists("env.py"):
    import env


creds = {
  "type": "service_account",
  "project_id": "pokemonspreadsheet",
  "private_key_id": os.environ.get("GPKID"),
#   "private_key": os.environ.get("GPK"),
  "client_email": os.environ.get("GSEMAIL"),
  "client_id": os.environ.get("GSID"),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.environ.get("CERT_URI")
}
print(creds)

# GSPREAD_CLIENT = gspread.service_account_from_dict(creds)
# SHEET = GSPREAD_CLIENT.open('Pokemon Card Spreadsheet')

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "pokemomCards"

app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "")

app.secret_key = os.environ.get("SECRET_KEY", "")

app.templates = ""

mongo = PyMongo(app)


@app.route('/')
def index():
    allSets = mongo.db.sets.find()
    return render_template("index.html", sets=allSets)

@app.route('/set/<set>')
def seeSet(set):
    sheet = SHEET.worksheet(set).get_all_values()
    return render_template("sets.html", cards=sheet)

@app.route('/update/<set>/<num>')
def updateCardInSet(set, num):
    if "user" in session:
        sheet = SHEET.worksheet(set)
        have = (sheet.get("B"+str(num)))
        if have:
            sheet.update("B"+str(num), "")
        else:
            sheet.update("B"+str(num), 1)
    return redirect("/")

@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        passwordIN = request.form.get("password")
        if passwordIN == os.environ.get("PASSWORD", ""):
            session["user"] = "admin"
            print(session["user"])
    return redirect("/")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 8080)),
            debug=True)