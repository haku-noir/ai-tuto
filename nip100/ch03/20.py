import json

def get_text(title, json_ary):
  for json_dict in json_ary:
    if json_dict["title"] == title:
      return json_dict["text"]

with open("jawiki-country.json") as f:
  l_ary = f.readlines()

json_ary = []
for l in l_ary:
  json_ary.append(json.loads(l))

print(get_text("イギリス", json_ary))
