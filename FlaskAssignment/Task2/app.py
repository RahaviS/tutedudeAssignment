from flask import Flask,render_template,request,jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def renderHtml():
    return render_template("index.html")

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["Organization"]
collection = db["Employees"]

@app.route("/submit", methods=["POST"])
def formSubmit():
    formData = request.form
    username = formData.get("name")
    password=formData.get("password")
    profession=formData.get("profession")
    jsonData = {
        "username":username,
        "password":password,
        "profession":profession
    }
    collection.insert_one(jsonData)
    return "Data Submitted Successfully"

if __name__ == "__main__":
    app.run(debug=True)