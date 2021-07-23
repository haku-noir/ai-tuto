import subprocess

f = open("popular-names.txt", "r")
l_ary = f.readlines()
f.close()

print("n = ", end="")
n = int(input())
s = ""
for i in range(0, n):
  s += l_ary[i]

print(s, end='')

res = subprocess.run(["./14.sh", str(n)], capture_output=True, text=True)
if s == res.stdout:
  print("Correct")
else:
  print("Incorrect")
