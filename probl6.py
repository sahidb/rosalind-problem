'''
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