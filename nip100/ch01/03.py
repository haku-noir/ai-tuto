s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
chars = "abcdefghijklmnopqrstuvwxyz"

c_chars = {}
for c in chars:
  c_chars[c] = 0

for c in s:
  if c.lower() in c_chars:
    c_chars[c.lower()] += 1

for c in chars:
  print(c + " " + str(c_chars[c]))
