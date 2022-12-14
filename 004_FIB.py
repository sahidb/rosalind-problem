'''
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n
months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''


# def fib(n, k):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1,k)+k*fib(n-2,k)
#
# print(fib(36,5))

def fib_loop(number):
    old, new = 1, 1
    for itr in range(number - 1):
        new, old = old, old + new
    return new


def fib_rabbits(months, offsprings):
    parrent, child = 1, 1
    for itr in range(months - 1):
        child, parrent = parrent, parrent + (child * offsprings)
    return child


print(fib_rabbits(5, 3))
