'''
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist,
then you may return any one of them.)
'''
from collections import Counter
# import numpy as np

def parse_fasta(s):
    results = {}
    strings = s.strip().split('>')

    for s in strings:

        if len(s) == 0:
            continue
        parts = s.split()
        # print(parts[2])
        label = parts[0]
        bases = ''.join(parts[1:])
        results[label] = bases
    return results


data = open("dataset/rosalind_cons.txt").read()
results = parse_fasta(data)
count_row = len(results)

list_value = []
profile = []
consensus_value = []
a = []
c = []
g = []
t = []

for value in results.values():
    list_value.append(value)

for i in range(len(list_value[0])):
    profile = []
    for j in range(len(list_value)):
        profile.append(list_value[j][i])
    count = Counter(profile)
    consensus_value.append(max(count, key=count.get))
    a.append(count['A'])
    c.append(count['C'])
    g.append(count['G'])
    t.append(count['T'])
    print(count)
    print(*profile, sep='')
    print('-------------')

print(*consensus_value, sep='')
print("A:", *a)
print("C:", *c)
print("G:", *g)
print("T:", *t)


