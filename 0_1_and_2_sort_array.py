# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

elements = [2, 0, 0, 1, 2, 0, 1, 1, 2, 0, 1]
n = len(elements)

low = 0
high = n - 1
mid = 0

while mid <= high:
    if elements[mid] == 0:
        elements[low], elements[mid] = elements[mid], elements[low]
        low += 1
        mid += 1

    elif elements[mid] == 2:
        elements[high], elements[mid] = elements[mid], elements[high]
        high -= 1

    else:
        mid += 1

print(elements)
