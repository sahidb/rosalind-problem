'''
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
'''
with open('./dataset/rosalind_revc.txt', 'r') as file:
    data = file.read().rstrip()

# dna='AAAACCCGGT'
# dna=dna[::-1]
dna = data[::-1]
# print(len(dna))
# print(dna)
new_dna =''
for x in dna:
    if x == 'A':
        new_dna += 'T'
    elif x =='T':
        new_dna+='A'
    elif x=='C':
        new_dna+='G'
    elif x=='G':
        new_dna+='C'
    else:
        new_dna += x

print(new_dna)