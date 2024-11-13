import yaml

with open ("task1/config.yaml", "r") as file:
    my_dict = yaml.safe_load(file)

my_dict["server"]["port"] = 9090

with open("task1/config.yaml", "w") as file:
    yaml.safe_dump(my_dict, file)

print("The port has been changed from 8080 to 9090")
