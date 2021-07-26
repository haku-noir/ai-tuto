import json
import re

def get_text(title, json_ary):
  for json_dict in json_ary:
    if json_dict["title"] == title:
      return json_dict["text"]

with open("jawiki-country.json") as f:
  l_ary = f.readlines()

json_ary = []
for l in l_ary:
  json_ary.append(json.loads(l))
uk_text = get_text("イギリス", json_ary)

p = re.compile(r"={2,4}.+={2,4}", re.MULTILINE)
s0_ary = p.findall(uk_text)
p_name = re.compile(r"[^=]+")
s_ary = []
for s0 in s0_ary:
  match_obj = p_name.search(s0)
  s = {}
  s["name"] = match_obj.group()
  s["level"] = match_obj.start() - 1
  s_ary.append(s)
print(s_ary)
