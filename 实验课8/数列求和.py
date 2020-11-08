n = int(input())
num = 0
if n%2 == 0:
    for i in range(2,n+2,2):
        num += 1/i
else:
    for i in range(1,n+2,2):
        num += 1/i
print("{:.2f}".format(num))
