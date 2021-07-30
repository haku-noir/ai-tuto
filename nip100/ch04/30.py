with open("neko.txt.mecab", "r") as f:
  l_ary = f.readlines()

s_ary = []
m_ary = []
for l in l_ary:
  if l == "EOS\n":
    s_ary.append(m_ary)
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

print(s_ary)
