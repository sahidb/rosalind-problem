'''
input:

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

output:
Rosalind_0808
60.919540
'''

import operator

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


def gc_content(s):
    n = len(s)
    m = 0
    for c in s:
        if c == 'G' or c == 'C':
            m += 1

    return 100 * (float(m) / n)

highest_v = 0
data = open("dataset/rosalind_gc.txt").read()
results = parse_fasta(data)

data_value = {label:gc_content(value) for label,value in results.items()}
print(data_value)

for i in max(data_value.items(), key=operator.itemgetter(1)):
    print(i)

