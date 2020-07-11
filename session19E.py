# JSON IN PYTHON
# json is a built in python module
# converts python dictionary into json
# OR reads json and converts it to python dictionary
import json

employee = {
    "name": "John",
    "phone": "+91 99999 11111",
    "salary": 30000
}

json_data = json.dumps(employee)
print(json_data)

dic_data = json.loads(json_data)
print(dic_data)