from random import shuffle

def random_word(w, l, r):
  ary_rnd = list(range(l, r))
  shuffle(ary_rnd)

  w_rnd = w[:l]
  for i in ary_rnd:
    w_rnd += w[i]
  w_rnd += w[r:len(w)]
  return w_rnd

print("s = ", end='')
s = input()
w_ary = s.split()

s_rnd = ""
for w in w_ary:
  if len(w) > 4:
    s_rnd += random_word(w, 1, len(w)-1)
  else:
    s_rnd += w
  s_rnd += " "
print(s_rnd)
