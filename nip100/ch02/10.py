import subprocess

f = open("popular-names.txt", "r")
l_ary = f.readlines()
f.close()
print(len(l_ary))

res = subprocess.run("./10.sh", capture_output=True)
if len(l_ary) == int(res.stdout):
  print("Correct")
else:
  print("Incorrect")
