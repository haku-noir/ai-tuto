import subprocess

f = open("popular-names.txt", "r")
l_ary = f.readlines()
f.close()
w_dict = {}
for l in l_ary:
  col1 = l.split()[0]
  if col1 in w_dict:
    w_dict[col1] += 1
  else:
    w_dict[col1] = 1

s = ""
for k in sorted(w_dict):
  s += k + "\n"
print(s, end="")

res = subprocess.run("./17.sh", capture_output=True, text=True)
if s == res.stdout:
  print("Correct")
else:
  print("Incorrect")
