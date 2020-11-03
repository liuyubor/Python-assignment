import random

def x():
    return random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])


n = int(input("请输入种子："))
random.seed(n)
print(x()+x()+x()+x()+x()+x())
