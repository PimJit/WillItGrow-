from flask import Flask, render_template, request
from willitgrow import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/result_page", method=["GET", "POST"])
def result_page():
    plant_name = request.form.get("plant_name")
    zipcode = request.form.get("zipcode")
    result_list = compare_plant_to_zone(fetchPlant(plant_name), zipcode_zone(zipcode), 1, plant_name)
