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

sorted_w_dict = sorted(w_dict.items(), key=lambda x: x[1], reverse=True)
max_digits = len(str(sorted_w_dict[0][1]))
s = ""
for x in sorted_w_dict: 
  s += "    "
  for i in range(0, max_digits-len(str(x[1]))):
    s += " "
  s += str(x[1]) + " " + x[0] + "\n"
print(s, end="")

res = subprocess.run("./19.sh", capture_output=True, text=True)
if s == res.stdout:
  print("Correct")
else:
  print("Incorrect")
