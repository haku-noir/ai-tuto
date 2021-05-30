from math import exp, log
from random import random

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

def inject(f, a):
  if len(a) == 0:
    return None

  val = a[0]
  for i in range(1, len(a)):
    val = f(val, a[i])
  return val

def collect(f, a):
  if len(a) == 0:
    return []

  val = [0] * len(a)
  for i in range(0, len(a)):
    val[i] = f(a[i])
  return val

def vecotr_operator(f, a, b):
  if len(a) != len(b):
    return None

  val = [0] * len(a)
  for i in range(0, len(a)):
    val[i] = f(a[i], b[i])
  return val

def sum(a):
  return inject(add, a)

def average(a):
  return sum(a) / len(a)

def scalar_mul(a, k):
  return collect(lambda a_i: a_i * k, a)

def v_sub(a, b):
  return vecotr_operator(sub, a, b)

def v_mul(a, b):
  return vecotr_operator(mul, a, b)

def inner＿product(a, b):
  return sum(v_mul(a, b))

def transpose(a):
  return [list(a_i) for a_i in zip(*a)]


def logistic(u):
  return 1 / (1 + exp(-u))

def cross_entropy(y, t):
  return -t * log(y) -(1-t) * log(1-y)

L = cross_entropy # loss function
f = logistic # activation function

E = 10000 # epoch
R = 1 / 100 # learning rate

N = 4 # 0 <= s < N # number of targets
n = 2 # 0 <= i < n # number of inputs

# t = [0] * N
t = [0, 1, 1, 1] # target (OR)
# t = [0, 0, 0, 1] # target (AND)
# x = [[0] * n] * N
x = [[0, 0], [0, 1], [1, 0], [1, 1]] # input

w = [random()] * n # weight
b = random() # bias

for e in range(0, E):
  output = lambda x: collect(lambda x_s: f(inner＿product(w, x_s) + b), x)
  y = output(x)
  # y = [f(w·x[0]+b), ···, f(w·x[N-1]+b)]

  adjust_i = lambda x_i: average(v_mul(v_sub(y, t), x_i))
  adjust = lambda x: collect(adjust_i, transpose(x))
  dL_dw = adjust(x)
  # dL_dw = [average((y-t)*x[0]), ···, average((y-t)*x[n-1])]
  w = v_sub(w, scalar_mul(dL_dw, R))

  dL_db = average(v_sub(y, t))
  b = b - R * dL_db

print(w, b)
for s in range(0, N):
  print(x[s], t[s], y[s], y[s] - t[s])
loss = vecotr_operator(L, y, t)
print(loss, average(loss))
