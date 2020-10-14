import turtle as t
# t.speed()
# 国旗轮廓
t.up()
t.back(144*2)
t.lt(90)
t.fd(81*2)
t.rt(90)
t.down()
t.fillcolor('red')
t.begin_fill()
t.fd(288*2)
t.rt(90)
t.fd(192*2)
t.rt(90)
t.fd(288*2)
t.rt(90)
t.fd(192*2)
t.end_fill()

# 大五角星
t.bk(76.8)
t.rt(90)
t.fd(38.4)
t.pencolor("yellow")  # 画笔黄色
t.fillcolor("yellow")  # 内部填充红色
t.begin_fill()  # 开始绘制
for _ in range(5):
    t.fd(115.2)
    t.rt(144)
t.end_fill()

# 绘制第一个小星
