from random import*

fc,cc,t=0,0,100000
for i in range(t):
	car=randint(0,2)
	guess=randint(0,2)
	if car==guess:
		fc+=1
	else:
		cc+=1
print("不改选择:{}".format(fc/t))
print("更改选择:{}".format(cc/t))