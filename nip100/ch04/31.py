def get_sentences():
  with open("neko.txt.mecab", "r") as f:
    l_ary = f.readlines()

  m_ary = []
  for l in l_ary:
    if l == "EOS\n":
      yield m_ary
      m_ary = []
      continue

    l_s = l.split("	")
    if len(l_s) != 2:
      continue
    m = l_s[0]
    m_info = l_s[1].split(",")

    m_ary.append({
      "surface": m,
      "base": m_info[6],
      "pos": m_info[0],
      "pos1": m_info[1]
    })

v_set = set()
for s in get_sentences():
  v_ary = list(filter(lambda x: x["pos"] == "動詞", s))
  if len(v_ary) > 0:
    v_ary = [m["surface"] for m in v_ary]
    v_set = v_set | set(v_ary)
print(v_set)
