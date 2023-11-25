#KMP rosalind

from Bio import SeqIO

seq_record = SeqIO.read('kmp.txt', 'fasta')
s = list(seq_record.seq)

failure = [0] * len(s)
k = 0

for i in range(1, len(s)):
    while k > 0 and s[k] != s[i]:
        k = failure[k - 1]
    if s[k] == s[i]:
        k += 1
    failure[i] = k


with open('output.txt', "w") as output:
    output.write(" ".join(map(str, failure)))


#python on my pc is unable to print more than a certain amount of characters, so i had to create a separate text file for the result
