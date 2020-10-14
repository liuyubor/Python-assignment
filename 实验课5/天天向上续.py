# daydayup 2.0

value, dayfactor = 1, 0.01
for i in range(365):
    if i % 7 in [4, 5, 6, 0]:
        value = value * (1+dayfactor)
print('最后的能力值为：{:.2f}'.format(value))
