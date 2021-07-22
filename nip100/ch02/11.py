import subprocess

f = open("popular-names.txt", "r")
s0 = f.read()
f.close()
s0 = str(s0)
s = ""
for i in range(0, len(s0)):
  if(s0[i] == "\t"):
    s += " "
  else:
    s += s0[i]

print(s, end='')

res = subprocess.run("./11.sh", capture_output=True, text=True)
if s == res.stdout:
  print("Correct")
else:
  print("Incorrect")
