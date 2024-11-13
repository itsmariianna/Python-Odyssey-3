import json

my_data = {
  "company": "TechCorp",
  "departments": [
    {
      "name": "Engineering",
      "employees": [
        {"id": 1, "name": "Alice", "role": "Engineer"},
        {"id": 2, "name": "Bob", "role": "Manager"}
      ]
    },
    {
      "name": "Sales",
      "employees": [
        {"id": 3, "name": "Charlie", "role": "Sales Rep"},
        {"id": 4, "name": "Dana", "role": "Sales Lead"}
      ]
    }
  ]
}


with open('task3/company_data.json', 'w') as json_file:
    json.dump(my_data, json_file, indent = 3)

print("Your data has been successfully added into json file")
