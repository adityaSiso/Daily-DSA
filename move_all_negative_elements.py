array = [-40, 2, -3, -10, -7, 30 , 22, 8, 91]

n = len(array)
low = 0
mid = 0

while mid < n:
    if array[mid] < 0:
        array[mid], array[low] = array[low], array[mid]
        low += 1
    mid += 1

print(array)

# Same as sort 0's, 1's, and 2's.
