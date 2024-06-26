# https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1

list_1 = [5, 3, 1, 7, 8]

list_1.insert(0, list_1.pop(-1))

print(list_1)

# Just remove the last element and add it at first position.
