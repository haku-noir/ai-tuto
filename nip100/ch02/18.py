import subprocess

f = open("popular-names.txt", "r")
l_ary = f.readlines()
f.close()
l_dict = {}
for l in l_ary:
  col3 = l.split()[2]
  l_dict[l] = int(col3)

s = ""
for x in sorted(l_dict.items(), key=lambda x: x[1], reverse=True):
  s += x[0]
print(s, end="")

res = subprocess.run("./18.sh", capture_output=True, text=True)
if s == res.stdout:
  print("Correct")
else:
  print("Incorrect")
