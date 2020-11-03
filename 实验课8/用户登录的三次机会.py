
for i in range(3):
    user = input("输入：\n")
    pwd = input()
    if user == "Kate" and pwd == "666666":
        print("登录成功！")
        break
    elif i == 2:
        print("3次用户名或者密码均有误！退出程序。")
        break
