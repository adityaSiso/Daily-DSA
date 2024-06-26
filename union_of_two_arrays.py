# https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1

list_1 = [5, 3, 1, 8, 7, 0]
list_2 = [3, 5, 8, 0, 1]

for number in list_1:
    if number not in list_2:
        list_2.append(number)

print(list_2)

# Each list has distinct numbers.
# Just check if the Ith number is present in the other list or not...
