import json

with open("task4/user_data.json", "r") as json_file:
    all_users = json.load(json_file)
    

def filtering(users):
    filtered_users = []
    for user in users:
        if user["role"] == "manager" and user["age"] > 30:
            filtered_users.append(user)
    return filtered_users


filtered_data = filtering(all_users)


with open("task4/filtered_users.json", "w") as new_json_file:
    json.dump(filtered_data, new_json_file, indent = 3)

print("New json file has been created with filtered data of users")