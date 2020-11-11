
def t(a):
    for i in range(5*a+1):
        if i % 5 == 0:
            print("+ {}".format(('- ' * 4+'+ ')*a))
        else:
            print("|{}".format((' '*9+'|')*a))


def main():
    a = eval(input("请输入格子数："))
    t(a)


main()
