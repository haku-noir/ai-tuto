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

p = re.compile(r'''
\{\{基礎情報 国
.*?
\}\}
$
''', re.MULTILINE | re.DOTALL)
s0_ary = p.search(uk_text).group().split("\n|")
s_dict = {}
for i in range(1, len(s0_ary)):
  s = re.sub(r"\'\'\'", "", s0_ary[i])
  s = re.sub(r"\*+", "", s)
  s = re.sub(r"\<br \/\>", "", s)
  s = re.sub(r"\<ref( name.*)?(\/)?\>(.+?\<\/ref\>)?", "", s)
  s = re.sub(r"\<\/ref\>", "", s)
  s = re.sub(r"\[\[ファイル\:", "", s)
  s = re.sub(r"\[https?\:.*\]", "", s, re.MULTILINE)
  s = re.sub(r"\{\{lang\|.+?\|", "", s, re.MULTILINE)
  s = re.sub(r"\{\{center\|", "", s, re.MULTILINE)
  s = re.sub(r"\{\{en icon\}\}", "", s, re.MULTILINE)
  s = re.sub(r"\}\}", "", s, re.MULTILINE)
  s = re.sub(r"\[\[[^\|\]]*?\|", "", s, re.MULTILINE)
  s = re.sub(r"\|[^\[]*?\]\]", "", s, re.MULTILINE)
  s = re.sub(r"\[\[", "", s, re.MULTILINE)
  s = re.sub(r"\]\]", "", s, re.MULTILINE)
  s = re.split(r"[ 　]*=[ 　]*", s)
  s_dict[s[0]] = s[1]
print(s_dict)
