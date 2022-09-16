'''
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
Sample Dataset

1 0 0 1 0 1

Sample Output

3.5

Probabilities of Child Dominant Genotype
----------------------------------------
s[0]: AA-AA -> 100% chance of dominant
s[1]: AA-Aa -> 100%
s[2]: AA-aa -> 100%
s[3]: Aa-Aa -> 75%
s[4]: Aa-aa -> 50%
s[5]: aa-aa -> 0%

'''

p_list = [1, 1, 1, 0.75, 0.5, 0]
EV_list=[]
with open('dataset/rosalind_iev.txt') as input_data:
	s = input_data.read().split()



# A simple application of expected value.
for index, num_parents in enumerate(s):
    EV_list.append(2*int(num_parents)*p_list[index])

print(sum(EV_list))
