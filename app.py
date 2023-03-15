from flask import Flask, render_template, request
from willitgrow import *
from TestData import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods=["GET", "POST"])
def result_page():
    try:
        plant_name = request.form.get("plant_name")
        zipcode = request.form.get("zipcode")
        result_list = compare_plant_to_zone(fetchPlant(plant_name), zipcode_zone(zipcode), 1, plant_name)
        final_list = []
        if request.method == "POST":
            for plant_id in result_list[0]:
                plant_dict = webDataRetrieve(plant_id, result_list[1])
                final_list.append(plant_dict)

            return render_template("result.html",  final_list=final_list)
        else:
            return "Error: was expecting a POST request", 400
    except Exception as e:
        print(e)

    # if request.method == "POST":
    #     plant1_id = plant_list1[0]
    #     plant2_id = plant_list1[1]
    #     plant3_id = plant_list1[2]
    #     plant4_id = plant_list1[3]
    #     plant5_id = plant_list1[4]
    #
    #     plant1_dict = webDataRetrieve1(plant1_id, plant_dict1)
    #     plant2_dict = webDataRetrieve1(plant2_id, plant_dict1)
    #     plant3_dict = webDataRetrieve1(plant3_id, plant_dict1)
    #     plant4_dict = webDataRetrieve1(plant4_id, plant_dict1)
    #     plant5_dict = webDataRetrieve1(plant5_id, plant_dict1)
    #
    #     return render_template("result.html",  plant1_dict=plant1_dict, plant2_dict=plant2_dict, plant3_dict=plant3_dict, plant4_dict=plant4_dict, plant5_dict=plant5_dict)
    # else:
    #     return "Error: was expecting a POST request", 400
