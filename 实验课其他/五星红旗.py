import turtle
def drawsnake(rad,angle,len,neckrad):
    colors = ['blue','purple','red','yellow']
    for i in range (len):
        turtle.pencolor(colors[i%4])
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle (neckrad+1,180)
    turtle.fd (rad*2/3)

def main ():
    turtle.setup (1366,768,0,0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.seth(-40)
    drawsnake(40,80,5,pythonsize/2)

main()
