'''
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
k individuals are homozygous dominant for a factor, m are heterozygous, and n
are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce
an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# k = homozygous dominant
# m = heterozygous
# n = homozygous recessive

input :
2 2 2

output :
0.78333
'''

import numpy as np

# 0 for dominant
# 1 for recessive

# alel
GG = np.array([[0, 0]])
Gg = np.array([[0, 1]])
gg = np.array([[1, 1]])
each_prob = []
each_dom_frac = []
sum_probs = []

def prob_dom(k, m, n):
    input = [k, m, n]
    for i in range(len(input)):
        for j in range(len(input)):
            t = k + m + n
            if i != j:
                probability = (input[i] / t) * (input[j] / (t - 1))
            else:
                probability = (input[i] / t) * ((input[j] - 1) / (t - 1))
            each_prob.append(probability)
    # print(each_prob)
    # print(sum(each_prob))
    for i in [GG, Gg, gg]:
        for j in [GG, Gg, gg]:
            mat = i.T * j
            dom_frac = np.sum(mat == 0) / 4.
            each_dom_frac.append(dom_frac)
    print(each_dom_frac)
    for n in range (len(input)**2):
        sum_probs.append(each_dom_frac[n]*each_prob[n])
    return sum(sum_probs)

# 17 27 20
print(prob_dom(17, 27, 20))
