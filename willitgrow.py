import urllib.parse, urllib.request, urllib.error, json
#Part 1: ask plant name and zipcode
plant_list_data = {}

#Part 2: get plant hardiness based on the zipcode from Frostline
def zipcode_zone(zipcode_input):
    try:
        zipcode_request = "https://phzmapi.org/"
        zipcode_request = zipcode_request + zipcode_input + ".json"
        response = urllib.request.urlopen(zipcode_request)
        zipcode_response_str = response.read()
        zipcode_data = json.loads(zipcode_response_str)
        hardiness_zone = int((zipcode_data['zone'])[0])
        return hardiness_zone
    except urllib.ertestror.URLError as e:
        print('Error from server. Error code: ', e.code)


#Part 3: get plants from Perenial
#plant_dict = {"key": }
plant_request = "https://perenual.com/api/species"
page_num = 1
temp_plant_list = {}

def fetch_plant_data(plant_name_input):
    try:
        url_request = "-list?page="+str(page_num)+"&key=sk-gneG64079b491eeca179"+"&q="+plant_name_input
        return json.loads(urllib.request.urlopen(url=plant_request+url_request).read())
    except urllib.error.URLError as e:
        print(str(e))
        return None

def fetchPlantHardness(id):
    url_request_id = json.loads(urllib.request.urlopen(url=plant_request+"/details/"+str(id)+"?key=sk-gneG64079b491eeca179").read())
    temp_plant_hard_min = int(url_request_id["hardiness"]["min"])
    temp_plant_hard_max = int(url_request_id["hardiness"]["max"])
    plant_list_data[id] = url_request_id
    return [temp_plant_hard_min, temp_plant_hard_max]

def fetchPlant(plant_name_input):
    data = fetch_plant_data(plant_name_input)
    if data == None:
        return None
    else:
        for plant in data["data"]:
            temp_plant_list[plant["id"]] = fetchPlantHardness(plant["id"])
        return (temp_plant_list)

#Part 4: compare the plant hardiness to zipcode hardiness
plant_list = []

def compare_plant_to_zone(temp_plant_list, hardiness_zone, page_num, plant_name_input):
    plant_dict = {}

    if temp_plant_list == None:
        return "Error: try a new plant search term"
    while len(plant_list) < 5:
        for plant in temp_plant_list:
            if temp_plant_list[plant][1] >= hardiness_zone >= temp_plant_list[plant][0]:
                plant_list.append(plant)
                plant_dict[plant] = plant_list_data[plant]
                if len(plant_list) == 5:
                    break
        temp_plant_list.clear()
        if page_num < 3:
            page_num += 1
            fetchPlant(plant_name_input)
        else:
            break
    return plant_list

compare_plant_to_zone(fetchPlant("fir"), zipcode_zone("98105"),1,"fir")
print(plant_list)

#plant_list = { plant key: [min,max], plant_key: [min,max], plant_key: [min,max] }
