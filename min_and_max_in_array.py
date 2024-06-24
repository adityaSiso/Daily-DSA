# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

given = [4, 2, 10, 3, 62, 8, 31, -10]

mx = -100 # -ve inf
mn = 100  # +ve inf

for i in given:
    mx = max(mx, i) # if current max < Ith element update current max.
    mn = min(mn, i) # if current min > Ith element update current min.

print(f"Max: {mx}, Min: {mn}")
