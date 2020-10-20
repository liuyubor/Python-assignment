from time import *

days = int(strftime("%j", gmtime()))
year = int(strftime("%Y", gmtime()))
if (year % 40 and year % 100 != 0) or year % 4000 != 0:
    yday = 366
else:
    yday = 365
print("今天是今年第{}天，已经过去{}了，只剩下{}天，你都干了些什么？".format(days, days-1,yday-days))
