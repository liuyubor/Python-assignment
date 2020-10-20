import datetime

def last(datastr):
    x = datetime.datetime.strptime(datastr, "%Y-%m-%d").strftime("%w")
    x = eval(x)
    datastr = datetime.datetime.strptime(datastr, "%Y-%m-%d")
    if x == 0:
        delta = datetime.timedelta(days=6)
        last = datastr - delta
    else:
        delta = datetime.timedelta(days=x+6)
        last = datastr - delta
    last = last.strftime("%Y-%m-%d")
    return last

def this(datastr):
    x = datetime.datetime.strptime(datastr, "%Y-%m-%d").strftime("%w")
    x = eval(x)
    datastr = datetime.datetime.strptime(datastr, "%Y-%m-%d")
    if x == 0:
        delta = datetime.timedelta(days=1)
        this = datastr + delta
    else:
        delta = datetime.timedelta(days=x-1)
        this = datastr - delta
    this = this.strftime("%Y-%m-%d")
    return this


def next(datastr):
    x = datetime.datetime.strptime(datastr, "%Y-%m-%d").strftime("%w")
    x = eval(x)
    datastr = datetime.datetime.strptime(datastr, "%Y-%m-%d")
    if x == 0:
        delta = datetime.timedelta(days=8)
        next = datastr + delta
    else:
        delta = datetime.timedelta(days=8-x)
        next = datastr + delta
    next = next.strftime("%Y-%m-%d")
    return next

n = input("请输入日期：")
print('上周一:', last(n))
print('本周一:', this(n))
print('下周一:', next(n))