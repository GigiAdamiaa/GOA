from turtle import*


#we want to paint a house

#step one: draw a square
width(7)
speed(30)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square

#step two: dwawinq a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20,120)
pendown()

color("blue")
begin_fill()
left(120)
forward(45)
left(90)
forward(55)
left(90)
forward(45)
left(90)
forward(55)
end_fill()

penup()
goto(130,120)
pendown()

begin_fill()
left(90)
forward(45)
left(90)
forward(55)
left(90)
forward(45)
left(90)
forward(55)
end_fill()




exitonclick()