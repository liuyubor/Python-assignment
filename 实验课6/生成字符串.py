strtemp = str(input("请输入一段字符："))
if(len(strtemp) < 2):
    print("Empty String")
else:
    print(strtemp[:2] + strtemp[-2:])
