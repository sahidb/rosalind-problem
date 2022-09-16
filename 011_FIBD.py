'''
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”,
which followed the recurrence relation Fn=Fn−1+Fn−2

and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male,
one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).
Given: Positive integers n≤100
and m≤20.

Return: The total number of pairs of rabbits that will remain after the n
-th month if all rabbits live for m months.
'''
import numpy as np

def f(n,m):
    population = np.zeros([n+1,m], dtype=np.int64)
    population[1][0] = 1

    for month in range(2,population.shape[0]):
        for age in range(0,population.shape[1]):
            if age == 0:
                population[month][age] = np.sum(population[month-1,1:])
            else:
                population[month][age] = population[month-1][age-1]

    return np.sum(population[n])

n = 86
m = 19
print(f(n,m))