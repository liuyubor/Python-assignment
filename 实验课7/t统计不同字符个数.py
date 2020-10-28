str = input("请输入一段字符：")
english = chinese = number = space = other = 0
for i in str:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        english += 1  # 英文计数
    elif 0x4e00 <= ord(i) <= 0x9fa5:
        chinese += 1  # 中文计数
    elif 48 <= ord(i) and ord(i) <= 57:
        number += 1  # 数字计数
    elif ord(i) == 32:
        space += 1
    else:
        other += 1
print("英文字符又{}个，中文字符有{}个，数字有{}个，空格有{}个，其他字符有{}个。".format(
    english, chinese, number, space, other))
