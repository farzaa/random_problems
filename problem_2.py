arr = [1, 2, 3, 4, 5]

# 1
output = []
for i in range(0, len(arr)):
    curr = 1
    for j in range(0, len(arr)):
        if i == j:
            continue
        curr = curr * arr[j]
    output.append(curr)
print("1 ", output)

# 2
output = []
from functools import reduce
for i in range(0, len(arr)):
    list_to_multiply = arr[0:i] + arr[i+1:]
    output.append(reduce(lambda x, y: x*y, list_to_multiply))
print("2 ", output)
