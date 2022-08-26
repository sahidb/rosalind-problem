
with open('./dataset/rosalind_rna.txt', 'r') as file:
    data = file.read().rstrip()
rna=data.replace('T','U')
print(rna)