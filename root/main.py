from flask import Flask
import json
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/kasutajad", methods=['POST'])
def kasutajad():
    kasutaja_vali = request.form.get("kasutaja")
    print(kasutaja_vali)
    return ""


# @app.route("/post_example", methods=['POST'])
# def hello_post_example():
#     users = json.loads(request.form.get("users"))  # makes string to dictionary
#
#     users["kasutajad"]  # asks from dictonary
#
#     print("Server! ", request.form.get("users"))
#     return ""
#
#
# def getTulemused():
#     return {"tulemused": ["tulemus"]}
#
#
# def getKasutajad():
#     return json.dumps(
#         {"kasutajad":
#             [
#                 {"kasutaja_nimi": "Lallu", "parool": ""},
#                 {"kasutaja_nimi": "Anu"},
#                 {"kasutaja_nimi": "Anni"}
#             ]
#         })
