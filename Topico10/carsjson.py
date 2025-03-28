import json

path = "./cars.json"

with open(path, "r") as f:
    data = json.load(f)
    for carros in data["cars"]:
        for key,value in carros.items():
            print(f"{key}: ",value)
        print("-----------")