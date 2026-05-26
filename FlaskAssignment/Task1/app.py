from flask import Flask
import json

app = Flask(__name__)

@app.route("/api")
def readJsonFile():
    file = open("data.json","r")
    data = json.load(file)
    file.close()
    return data

if __name__ == "__main__":
    app.run(debug=True)


