import random
a, i = random.randint(0, 100), 0
while True:
    num = eval(input("请猜一个数字:"))
    i += 1
    if a == num:
        print("预测%d次，你猜中了！" % i)
        break
    elif num > a:
        print("遗憾，太大了")
    else:
        print("遗憾，太小了")
