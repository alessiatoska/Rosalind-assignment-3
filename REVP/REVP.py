#REVP rosalind

from Bio import SeqIO

records = list(SeqIO.parse("revp.txt", "fasta"))
seq = str(records[0].seq)

def revc(seq):
    return seq[::-1].translate(str.maketrans('ACGT', 'TGCA'))

for i in range(len(seq)):
    for j in range(4, min(13, len(seq)-i+1), 2):
        if seq[i:i+j] == revc(seq[i:i+j]):
            print(i+1, j)

