import numpy as np

def logistic(u):
  return 1 / (1 + np.exp(-u))

def cross_entropy(y, t):
  return np.add(-t * np.log(y), -(1-t) * np.log(1-y))

L = cross_entropy
f = logistic

E = 10000
R = 1 / 100

N = 4
n = 2

t = np.array([0, 1, 1, 1])
# t = np.array([0, 0, 0, 1])
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

w = np.random.randn(n)
b = np.random.randn(1)

for e in range(0, E):
  u = np.dot(x, w) + b
  y = f(u)

  dL_dw = np.mean((y - t) * np.transpose(x))
  w = w - R * dL_dw

  dL_db = np.mean(y - t)
  b = b - R * dL_db

print(w, b)
for s in range(0, N):
  print(x[s], t[s], y[s], y[s] - t[s])
loss = L(y, t)
print(loss, np.mean(loss))
