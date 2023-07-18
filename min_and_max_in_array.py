# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

given = [4, 2, 10, 3, 62, 8, 31, -10]

mx = -1
mn = 100

for i in given:
    mx = max(mx, i)
    mn = min(mn, i)

print(f"Max: {mx}, Min: {mn}")
