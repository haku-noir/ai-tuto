def cut(filename, idx):
  f = open(filename, "r")
  l_ary = f.readlines()
  f.close()
  col = ""
  for l in l_ary:
    row = l.split()
    col += row[idx-1] + "\n"
  return col

def fread(filename):
  f = open(filename, "r")
  s = f.read()
  f.close()
  return s

def fwrite(filename, s):
  f = open(filename, "w")
  f.write(s)
  f.close

col1 = cut("popular-names.txt", 1)
col2 = cut("popular-names.txt", 2)
fwrite("col1-py.txt", col1);
fwrite("col2-py.txt", col2);

col1_py = fread("col1-py.txt")
col1_sh = fread("col1.txt")
col2_py = fread("col2-py.txt")
col2_sh = fread("col2.txt")

if col1_py == col1_sh and col2_py == col2_sh:
  print("Correct")
else:
  print("Incorrect")
