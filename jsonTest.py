import json

data = {
    "Abbot's Jo Staff": {
        "name": "Abbot's Jo Staff",
        "type": "Staffy/Smashy",
        "bonus": "Will",
        "damage": "116",
        "level": "40"
    },
    "Acheron Set": {
        "name": "Acheron Set",
        "type": "Shooty/Slashy",
        "bonus": "Agility",
        "damage": "191",
        "level": "55"
    }
}

with open("data.json", "w") as write_file:
    json.dump(json.dumps(data, indent=1), write_file)

with open("data.json", "r") as read_file:
    data = json.load(read_file)
    print(data)