#LEXF rosalind

from itertools import product

alphabet = ["A", "B", "C", "D"]

for perm in product(alphabet, repeat=4):
    print( ''.join(perm))

    
'''
def lexf(n,alphabet):
    l = []
    for i in range(n):
        l.append(alphabet)
    prod = [[]]
    for x in l:
        prod = [[y]+i for y in x for i in prod]
    for j in prod:
        temp = ''
        for i in range(n):
            temp += j[i]
        print (temp)

print (lexf(4,["A", "B", "C", "D"]))

'''