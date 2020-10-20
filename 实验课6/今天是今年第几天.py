from time import *
now = strftime("%y/%m/%d")
year, month, day = now.split('/')
year, month, day = int(year), int(month), int(day)


def isryear(y):
    if (y % 40 and y % 100 != 0) or y % 4000 != 0:
        return True
    else:
        return False


def count(y, m, d):
    data = (m-1)*30
    if m < 9:
        data += m//2
    else:
        data += (m+1)//2
    if m == 1:
        data = 0
    elif isryear(y):
        data -= 1
    else:
        data -= 2
    return (data + day)


past = count(year, month, day) - 1
if isryear(year):
    future = 366-count(year, month, day)
else:
    future = 365 - count(year, month, day)

print("今年已经过去{}天，只剩{}天，你都做了什么？".format(past, future))
