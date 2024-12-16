import numpy as np

def f(x):
  return x**2 - 10 * np.sin(x) -2

def df(x):
  return 2 * x - 10*np.cos(x) 

x=0.7
accuracy=0.001
n=1
# while文でf(x)=0まで繰り返す
while True:
  x = x - f(x)/df(x)
  print("{}回目  x={}  f(x)={}".format(n, x, f(x)))
  n += 1
  if abs(f(x)) < accuracy:
    break 

print(str(x))