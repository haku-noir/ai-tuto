import subprocess

def split(filename, n, f_head, f_tail):
  f = open(filename, "r")
  l_ary = f.readlines()
  f.close()
  l_num = len(l_ary)
  i = 1
  for i in range(1, n+1):
    s = ""
    for j in range(0, int(l_num/n)):
      s += l_ary[i*n+j]
    fwrite(f_head + fig2(i) + f_tail, s)
  if l_num % n != 0:
    s = ""
    for j in range(0, l_num%n):
      s += l_ary[i*n+j]
    fwrite(f_head + fig2(i) + f_tail, s)
  return s

def fread(filename):
  f = open(filename, "r")
  s = f.read()
  f.close()
  return s

def fwrite(filename, s):
  f = open(filename, "w")
  f.write(s)
  f.close

def fig2(x):
  if x <= 0 or x > 99:
    return "00"
  if x < 10:
    return "0" + str(x)
  return str(x)

print("n = ", end="")
n = int(input())
split("popular-names.txt", n, "popular-names-", "-py.txt")
res = subprocess.run(["./16.sh", str(n)], capture_output=True, text=True)

corr = True
for i in range(1, n+1):
  s_py = fread("popular-names-" + fig2(i) + "-py.txt")
  s_sh = fread("popular-names-" + fig2(i) + ".txt")
  if s_py != s_py:
    corr = False
    break
if corr:
  print("Correct")
else:
  print("Incorrect")
