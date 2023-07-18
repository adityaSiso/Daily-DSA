# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

given = [5, 2, 8, 1, 7, 0]
n = len(given)

for i in range(n//2):
    given[i], given[n - i - 1] = given[n - i - 1], given[i]

print(given)
