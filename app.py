'''
Source:

Author: Raja CSP


'''
from flask import Flask, render_template, jsonify
import random
import json

app  = Flask(__name__)
PORT = 3000

FILEPATH = "data.json"
    
'''
    http://0.0.0.0:3000/

    https://www.youtube.com/watch?v=wgfc07NJskY
'''
@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    return render_template("index.html")

'''
    http://0.0.0.0:3000/data

'''
@app.route("/data", methods=["GET","POST"])
def read_json():

    with open(FILEPATH) as json_file:
        data = json.load(json_file)

    # print(data)

    return jsonify(data)

    # return render_template("index.html", result = data)

if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)
    