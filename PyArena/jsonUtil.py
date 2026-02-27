import json

inJson = '''{"id": 235,
  "brand": "Nike",
  "qty": 84,
  "status": {
    "isForSale": true
  }
}'''

dic = {"name": "Victor", "qty": 25}
outJson = json.dumps(dic, indent=4)
print(outJson)

# inArray = '[{"a":1}, {"b":2}, {"c":3}]'
# lst = json.loads(inArray)
# print(lst)
# print(lst[2]["c"])

# dic = json.loads(s)
# print(dic["status"])
