# 小于五十就退出
def putin():
    num = eval(input('请输入一个数：'))
    return num

num = 0
while( putin() < 50):
    print('小于五十。')
