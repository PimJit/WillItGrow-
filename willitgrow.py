import urllib.parse, urllib.request, urllib.error, json
#Part 1: ask plant name and zipcode
plant_name_input = "fir"
zipcode_input = "98105"

#Part 2: get plant hardiness based on the zipcode from Frostline
#A: get url, request, loads, and return the json data
zipcode_request = "https://phzmapi.org/"
zipcode_request = zipcode_request + zipcode_input + ".json"

response = urllib.request.urlopen(zipcode_request)
zipcode_response_str = response.read()
zipcode_data = json.loads(zipcode_response_str)

#B: specifically get the hardiness as a variable
hardiness_zone = zipcode_data['zone']


#Part 3: get plants from Perenial
#plant_dict = {"key": }
plant_request = "https://perenual.com/api/species"
page_num = 1
temp_plant_list = {}

def fetch_plant_data():
    try:
        url_request = "-list?page="+str(page_num)+"&key=sk-gneG64079b491eeca179"+"&q="+plant_name_input
        print(plant_request+url_request)
        return json.loads(urllib.request.urlopen(url=plant_request+url_request).read())
    except urllib.error.URLError as e:
        print(str(e))
        return None

def fetchPlantHardness(id):
    url_request_id = json.loads(urllib.request.urlopen(url=plant_request+"/details/"+str(id)+"?key=sk-gneG64079b491eeca179").read())
    temp_plant_hard_min = url_request_id["hardiness"]["min"]
    temp_plant_hard_max = url_request_id["hardiness"]["max"]
    return [temp_plant_hard_min, temp_plant_hard_max]

def fetchPlant():
    data = fetch_plant_data()
    for plant in data["data"]:
        temp_plant_list[plant["id"]] = fetchPlantHardness(plant["id"])

fetchPlant()
print(temp_plant_list)
#Part 4: compare the plant hardiness to zipcode hardiness

#Part 5: repeat until we get 5 plants that matches the hardiness zone

#Part 6: return list of plants

