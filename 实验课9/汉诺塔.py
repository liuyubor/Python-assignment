import time


def hanoi(n, p1, p2, p3):
    n = int(n)
    if n == 1:
        print('盘子从{}移到{}'.format(p1, p3))
        return None
    else:
        hanoi(n-1, p1, p3, p2)
        print('盘子从{}移到{}'.format(p1, p3))
        hanoi(n-1, p2, p1, p3)


a = time.time()
n = input("请输入盘子数量：")
p1, p2, p3 = 'A', 'B', 'C'
hanoi(n, p1, p2, p3)
b = time.time() - a
print("程序执行了{:.3f}秒".format(b))
