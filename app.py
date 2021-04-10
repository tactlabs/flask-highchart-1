'''
Source:

Author: Raja CSP


'''
from flask import Flask, render_template, jsonify
import random
import json

app  = Flask(__name__)
PORT = 3001

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
@app.route("/data", methods=["GET"])
def read_json():

    data = None
    with open(FILEPATH) as json_file:
        data = json.load(json_file)

    # print(data)

    # print(data.keys())

    months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    temp_list = [33, 38, 43, 20, 39, 35, 32, 35, 36, 38, 29, 45]

    result_dict = {
        'months'        : months_list,
        'local_data'    : data,
        'city'          : 'Chennai',
        'title'         : 'Monthly Average Temperature',
        'subtitle'      : 'Source: WorldClimate.com',
        'temp_data'     : temp_list 
    }

    return jsonify(result_dict)

    # return render_template("index.html", data = data)

if __name__ == "__main__":
    app.run( debug = True, host="0.0.0.0", port = PORT)
    