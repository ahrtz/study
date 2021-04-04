import itertools
prices=[1,2,3,4,5]

a=itertools.combinations(prices,3)
for i in a:
    print(i)
