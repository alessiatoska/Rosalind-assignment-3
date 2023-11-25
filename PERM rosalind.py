#PERM rosalind

from itertools import permutations

n = 3

def perm(n):
    permutation = list(permutations(range(1, n+1)))
    total_permutations = len(permutation)
    return total_permutations, permutation

total_perm = perm(n)[0]
print(total_perm)

for i in perm(n)[1]:
    print(" ".join(map(str, i)))

