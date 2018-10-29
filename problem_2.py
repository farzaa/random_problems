arr = [1, 2, 3, 4, 5]

output = []
for i in range(0, len(arr)):
    curr = 1
    for j in range(0, len(arr)):
        if i == j:
            continue
        curr = curr * arr[j]
    output.append(curr)
print(output)
