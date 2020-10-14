num = 0
for i in range(1, 10+1):
    value = 1
    for j in range(1, i+1):
        value *= j
    num += value
print(num)
