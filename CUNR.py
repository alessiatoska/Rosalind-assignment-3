#CUNR rosalind

from math import prod

n=855
modulo=1000000

print(prod(range((2*n - 5), 0, -2)) % modulo)

'''
n = 855
modulo = 1000000
result = 1

for i in range(2 * n - 5, 0, -2):
    result = (result * i) % modulo

print(result)

'''
