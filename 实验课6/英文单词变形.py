
strtemp = input("请输入一个英文单词:")
if(strtemp[-3:] == "ing"):
    print(strtemp + "ly")
elif(len(strtemp) < 3):
    print(strtemp)
else:
    print(strtemp + "ing")
