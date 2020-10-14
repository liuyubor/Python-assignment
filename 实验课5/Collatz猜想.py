# Collztz猜想

num = int(input())
while(num != 1):
    if (num % 2 == 0):  # 判断为偶数
        num /= 2
        print(num)
    else:
        num = num*3 + 1
        print(num)
