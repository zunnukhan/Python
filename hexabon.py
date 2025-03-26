import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,300)
polygon=turtle.Turtle()
polygon.speed(1)
numsides=6
sidelength=70
angle=360.0/numsides  
for i in range (numsides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()