'''
input :
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

output :
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323

 A A A T T T T
 0 1 2 3 4 5 6
-7-6-5-4-3-2-1
'''

from Bio import SeqIO

seq_n, seq_s = [], []
n = 3
data = open("dataset/rosalind_grph.txt",'r')
for seq_rec in SeqIO.parse(data,'fasta'):
    seq_n.append(str(seq_rec.name))
    seq_s.append(str(seq_rec.seq))

for i in range(len(seq_s)):
    for j in range(len(seq_s)):
        if i != j:
            if seq_s[i][-n:] == seq_s[j][:n]:
                print(seq_n[i], seq_n[j])
print(seq_s[1])
print(seq_s[1][-3:])



