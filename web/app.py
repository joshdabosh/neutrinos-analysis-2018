import NeutrinoBlazarMatching as nbm

from flask import Flask, request, redirect
from flask_cors import CORS, cross_origin

import json

app = Flask(__name__)

cors = CORS(app)

app.config["CORS_HEADERS"] = "Content-Type"

@app.route("/")
def index():
  return redirect("https://banjo.joshdabosh.repl.co", code=200)

@app.route("/getResults", methods=["GET", "POST"])
def getResults():
  if request.method == "POST":
    d = json.loads(request.data.decode("utf-8"))

    ra = float(d["ra"])
    de = float(d["dec"])

    a, v, t = nbm.main(ra, de, verbose=False)
    
    ret = json.dumps(v)

    return ret

app.run(host="0.0.0.0", port=8000)
