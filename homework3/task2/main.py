import yaml
import json

with open("task2/mydata.yaml", "r") as file:
    yaml_data = yaml.safe_load(file)

with open("task2/data.json", "w") as json_file:
    json.dump(yaml_data, json_file, indent = 3)

print("The data from yaml file is now in json file.")
