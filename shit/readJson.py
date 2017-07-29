import json, pprint
with open('info.json') as data_file:
    data = json.load(data_file)

pprint.pprint(data)

print(data["houses"][0])
print(data["houses"][1])
print(data["characteristics"]["name"])
print(data["characteristics"]["weight"])
print(data["characteristics"]["niceperson"])
print(type(data))