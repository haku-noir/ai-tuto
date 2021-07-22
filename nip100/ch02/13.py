def paste(filename1, filename2):
  f = open(filename1, "r")
  l_ary1 = f.readlines()
  f.close()
  f = open(filename2, "r")
  l_ary2 = f.readlines()
  f.close()
  s = ""
  for i in range(0, len(l_ary1)):
    s += l_ary1[i][:len(l_ary1[i])-1] + "\t" + l_ary2[i]
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

col_1_2 = paste("col1-py.txt", "col2-py.txt")
fwrite("popular-names-1-2-py.txt", col_1_2)

col_1_2_py = fread("popular-names-1-2-py.txt")
col_1_2_sh = fread("popular-names-1-2.txt")

if col_1_2_py == col_1_2_sh:
  print("Correct")
else:
  print("Incorrect")
