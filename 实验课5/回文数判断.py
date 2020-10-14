# 回文数判断

n = input('请输入一个五位数字：')
x = eval(n[::-1])
y = eval(n)
if (x == y):
    print('{}是回文字'.format(n))
else:
    print('{}不是回文字'.format(n))
