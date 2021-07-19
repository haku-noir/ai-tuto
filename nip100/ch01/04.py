s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s_ary = s.split()
chars = [1, 5, 6, 7, 8, 9, 15, 16, 19]

element = {}
for i in range(len(s_ary)):
  r = 2
  if(i + 1 in chars):
    r = 1
  element[s_ary[i][0:r]] = i + 1

print(element)
