import json

my_data = {
    "name": "Ola",
    "age": 20,
    "home": "Gabin",
    "hobby": "chess",
}

# json_object_my_data = json.dumps(my_data, indent=4)
# with open("test_json.json", "w") as filehandle:
#     filehandle.write(json_object_my_data)

with open("test_json.json", "w") as filehandle:
    json.dump(my_data, filehandle, indent=4)

# with open("test_json.json", "r") as filehandle:
#     data = json.load(filehandle)

# print(data)
# print(data["name"])