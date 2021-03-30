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
@app.route("/data", methods=["GET"])
def read_json():

    data = None
    with open(FILEPATH) as json_file:
        data = json.load(json_file)

    # print(data)

    months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    temp_list = [120, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 23, 23.3, 18.3, 13.9, 9.6]

    result_dict = {
        'months' : months_list,
        'local_data' : data,
        'city' : 'Toronto',
        'title' : 'Monthly Average Temperature',
        'subtitle' : 'Source: WorldClimate.com',
        'temp_data' : temp_list 
    }

    return jsonify(result_dict)

    # return render_template("index.html", result = data)

if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)
    