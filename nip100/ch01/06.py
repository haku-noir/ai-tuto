import collections

def ngram(n, w_ary):
  if len(w_ary) < n+1:
    return None
  ngram = []
  for i in range(len(w_ary)-n+1):
    ngram.append(w_ary[i:i+n])
  return ngram

def unique_list(list):
  return [k for k, v in collections.Counter(list).items() if v >= 1]

def difference(s1, s2):
  s = []
  for s1_i in s1:
    exist = True
    for s2_j in s2:
      if s1_i == s2_j:
        exist = False
    if exist:
      s.append(s1_i)
  return s

def intersection(s1, s2):
  return difference(s1, difference(s1, s2))

def union(s1, s2):
  return s1 + (difference(s2, s1))

s1 = "paraparaparadise"
s2 = "paragraph"

X = ngram(2, s1)
Y = ngram(2, s2)
X = unique_list(X)
Y = unique_list(Y)

print(X)
print(Y)
print(union(X, Y))
print(difference(X, Y))
print(intersection(X, Y))
