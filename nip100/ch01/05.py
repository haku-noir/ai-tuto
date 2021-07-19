from functools import reduce

split_chars = ['.', ',']

def words2str(w_ary):
  return reduce(lambda w1, w2: w1 + w2, w_ary)

def str2words(s0):
  s = ""
  for c in s0:
    if c in split_chars:
      s += ' '
    s += c
  return s.split()

def ngram(n, w_ary):
  if len(w_ary) < n+1:
    return None
  ngram = []
  for i in range(len(w_ary)-n+1):
    ngram.append(w_ary[i:i+n])
  return ngram

print("n = ", end='')
n = int(input())
print("s = ", end='')
s = input()

print(ngram(n, s))
print(ngram(n, str2words(s)))
