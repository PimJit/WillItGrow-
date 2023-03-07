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

#Part 4: compare the plant hardiness to zipcode hardiness

#Part 5: repeat until we get 5 plants that matches the hardiness zone

#Part 6: return list of plants

