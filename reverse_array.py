# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

given = [5, 2, 8, 1, 7, 0]
n = len(given)

for i in range(n//2):
    given[i], given[n - i - 1] = given[n - i - 1], given[i]

print(given)

"""
5, 3, 8, 1, 0 -> 0, 1, 8, 3, 5

Array: 5, 3, 8, 1, 0
Index: 0, 1, 2, 3, 4 -> 0 <-> 4, 1 <-> 3, <2>

swap index i and n-i.
"""
