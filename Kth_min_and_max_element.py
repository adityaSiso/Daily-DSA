# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1

elements = [10 , 4, 55, 21, 89, 101, 3, -12, 15]
Kth = 3

elements.sort() #Time complexity is nlog(n)
print(f'{Kth} max element is {elements[-3]}')
print(f'{Kth} min element is {elements[2]}')

# Solution 1: Just sort and fetch the Kth[Kth - 1 in python] index element.
# Solution 2: :-/
