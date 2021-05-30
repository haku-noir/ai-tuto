using LinearAlgebra
using Statistics

function logistic(u::Number)::Float64
  return 1 / (1 + exp(-u))
end

function cross_entropy(y::Number, t::Number)::Float64
  return -t * log(y) -(1-t) * log(1-y)
end

L = cross_entropy
f = logistic

E = 10000
R = 1 / 100

N = 4
n = 2

t = [0,
     1,
     1,
     1]
# t = [0, 0, 0, 1]
x = [0 0;
     0 1;
     1 0;
     1 1]

w = randn(Float64, 2)
b = randn(Float64)

for e = 1:E
  u = x * w .+ b
  y = f.(u)

  dL_dw = mean.(x' * (y - t))
  global w = w - R .* dL_dw

  dL_db = mean(y - t)
  global b = b - R * dL_db
end

println("$w $b")
y = f.(x * w .+ b)
for s = 1:N
  println("$(x[s]) $(t[s]) $(y[s]) $(y[s] - t[s])")
end
loss = L.(y, t)
println("$loss $(mean(loss))")
