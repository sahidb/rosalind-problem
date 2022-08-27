'''
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n
months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''

def fib(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1,k)+k*fib(n-2,k)

print(fib(5,3))