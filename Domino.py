from turtle import *

title('Domino')
speed(2)
pensize(5)
bgcolor('indigo')

penup()
goto(-100, 0)
pendown()

# Squares
color('#333333', 'white')
begin_fill()

for i in range(4):
    forward(200)
    right(90)

left(90)

for i in range(3):
    forward(200)
    right(90)
end_fill()

# Top circle

penup()
goto(0, 130)
pendown()
color('#333333')
begin_fill()
circle(30)
end_fill()

# Bottom Circles

penup()
goto(-50, -20)
pendown()
color('#333333')
begin_fill()
circle(30)
end_fill()

penup()
goto(50, -120)
pendown()
color('#333333')
begin_fill()
circle(30)
end_fill()

hideturtle()
exitonclick()
