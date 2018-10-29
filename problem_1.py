arr = [7, -15, 3, 10]
k = -12

seen = {}
for num in arr:
    seen[num] = num
    if (k - num) in seen:
        print("True")



