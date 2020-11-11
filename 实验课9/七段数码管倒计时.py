import turtle
import time


def drawGap():  # 绘制间隔
    turtle.penup()
    turtle.fd(5)


def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)


def drawDigit(d):  # 根据数字绘制七段数码管
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def main(t):
    turtle.hideturtle()
    turtle.pencolor("red")
    turtle.penup()
    turtle.delay(0)
    turtle.pensize(5)
    turtle.setpos(0, 0)
    while t > -1:
        for i in str(t):
            drawDigit(int(i))
        time.sleep(1)
        t = t - 1
        turtle.clear()
        turtle.setpos(0, 0)


t = eval(input("输入时间："))
main(t)
