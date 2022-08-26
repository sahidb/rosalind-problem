with open('./dataset/rosalind_dna.txt', 'r') as file:
    data = file.read().rstrip()
A=data.count('A')
G=data.count('G')
T=data.count('T')
C=data.count('C')

print(A,C,G,T)

