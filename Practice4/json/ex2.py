import json
text = '{"name": "Ali", "age": 20}'
data = json.loads(text)
print(data["name"])