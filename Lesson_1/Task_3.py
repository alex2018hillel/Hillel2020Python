import numpy as np

def decomposition(n):
   i = 2
   str_decomposition = []
   decomposition = []
   while i * i <= n:
       while n % i == 0:
           decomposition.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       decomposition.append(n)
   frequency = dict(zip(*np.unique(decomposition, return_counts=True)))
   for key, value in frequency.items():
       if value != 1:
            factor = str(int(key)) + "^" + str(value)
       else:
            factor = str(int(key))
       str_decomposition.append(factor)
   return "*".join(map(str, str_decomposition))

n=int(input("Integer: "))
print(decomposition(n))

