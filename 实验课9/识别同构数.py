x = []
while True:
    s = input("")
    if s == "-1":
        break
    elif len(s) > 2 or (not (s.isdigit())):
        print("请输入如不超过两位数的正整数！")
        continue
    else:
        a = str(int(s)**2)
        b = len(s)
        c = 1
        for i in range(-1, -b-1, -1):
            if a[i] != s[i]:
                c = 0
                break
        if c:
            x.append(int(s))
x.sort()
print("同构数有：", end='')
for i in x:
    print(i, end=' ')
