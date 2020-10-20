from time import *

timestr = input("请输入格式为2020.10.20的任意日期:")
#strptime(timestr,"%Y-%m-%d") # strptime把信息传递到struct_time对象
t = timestr.split('.')
year = int(t[0])
mon = int(t[1])
day = int(t[2])

yday = eval(struct_time.tm_yday)
day = yday - week

strptime(day,"%j")
data = strftime("%Y-%m-%d", struct_time)

strptime(day-7,"%j")
pdata = strftime("%Y-%m-%d", struct_time)

strptime(day+7,"%j")
ldata = strftime("%Y-%m-%d", struct_time)

print("上周一为{}，本周一为{}，下个周一为{}。".format(pdata,data,ldata))
