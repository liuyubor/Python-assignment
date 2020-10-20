def zodiac(year):
    sx = {0: "鼠", 1: "牛", 2: "虎", 3: "兔", 4: "龙", 5: "蛇",
          6: "马", 7: "羊", 8: "猴", 9: "鸡", 10: "狗", 11: "猪"}
    return sx[(year - 1984) % 12]


def constellation(month, day):
    d = (20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22)
    c = ("摩羯座", "水瓶座", "双鱼座", "白羊座", "金牛座", "双子座",
         "巨蟹座", "狮子座", "处女座", "天秤座", "天蝎座", "射手座")
    if day < d[month-1]:
        return c[month-1]
    else:
        return c[month]


birthday = input("请输入格式为2020.10.20的生日日期:")
t = birthday.split('.')
year = int(t[0])
month = int(t[1])
day = int(t[2])

print("您的生肖为{}，星座为{}".format(zodiac(year), constellation(month, day)))
