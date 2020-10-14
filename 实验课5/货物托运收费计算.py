# 货物托运费计算

weight = eval(input('输入货物重量：'))
if(weight <= 50):
    price = weight * 0.5
else:
    price = 25 + (weight-50)*0.6
print(price)
