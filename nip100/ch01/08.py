def cipher(s0):
  s = ""
  for s_i in s0:
    if(s_i.islower()):
      s += chr(219 - ord(s_i))
    else:
      s += s_i
  return s

print("s = ", end='')
s = input()
print(cipher(s))
print(cipher(cipher(s)))
