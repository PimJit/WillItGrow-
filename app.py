from flask import Flask, render_template, request
# from willitgrow import *
from TestData import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods=["GET", "POST"])
def result_page():
    # plant_name = request.form.get("plant_name")
    # zipcode = request.form.get("zipcode")
    # # result_list = compare_plant_to_zone(fetchPlant(plant_name), zipcode_zone(zipcode), 1, plant_name)
    # result_list = [plant_list1, plant_dict1]
    # if request.method == "POST":
    #     plant1_id = result_list[0][0]
    #     plant2_id = result_list[0][1]
    #     plant3_id = result_list[0][2]
    #     plant4_id = result_list[0][3]
    #     plant5_id = result_list[0][4]
    #     plant1_dict = webDataRetrieve(plant1_id, result_list[1])
    #     plant2_dict = webDataRetrieve(plant2_id, result_list[1])
    #     plant3_dict = webDataRetrieve(plant3_id, result_list[1])
    #     plant4_dict = webDataRetrieve(plant4_id, result_list[1])
    #     plant5_dict = webDataRetrieve(plant5_id, result_list[1])
    # else:
    #     return "Error: was expecting a POST request", 400

    if request.method == "POST":
        plant1_id = plant_list1[0]
        plant2_id = plant_list1[1]
        plant3_id = plant_list1[2]
        plant4_id = plant_list1[3]
        plant5_id = plant_list1[4]

        plant1_dict = webDataRetrieve1(plant1_id, plant_dict1)
        plant2_dict = webDataRetrieve1(plant2_id, plant_dict1)
        plant3_dict = webDataRetrieve1(plant3_id, plant_dict1)
        plant4_dict = webDataRetrieve1(plant4_id, plant_dict1)
        plant5_dict = webDataRetrieve1(plant5_id, plant_dict1)

        return render_template("result.html",  plant1_dict=plant1_dict, plant2_dict=plant2_dict, plant3_dict=plant3_dict, plant4_dict=plant4_dict, plant5_dict=plant5_dict)
    else:
        return "Error: was expecting a POST request", 400
