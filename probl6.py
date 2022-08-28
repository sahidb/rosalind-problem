'''
Given: Two DNA strings s and t

of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)
.

input :
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

output :
7
'''

def hamming_dist(s,t):
    dist = 0
    for i,v in enumerate(s):
        if v != t[i]:
            dist+=1
    return dist

string = open("dataset/rosalind_hamm.txt").read()
s,t = string.split()
print(hamming_dist(s,t))