import json
filename = "wsaa2.4-json.json"

with open(filename, "r") as fp:
    jsonobject = json.load(fp)
#print (jsonobject)
for employee in jsonobject["employees"]:
    print(employee["firstName"])

#  This code reads the JSON file wsaa2.4-json.json and prints the first names of the employees.