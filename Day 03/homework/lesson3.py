from turtle import*

speed(30)
width(3)
#ვიწყებ მზის ხატვა
penup()
goto(250,250)
pendown()

color("yellow")
begin_fill()
circle(50)
end_fill()

right(90)
forward(35)
left(180)
forward(85)
left(90)
forward(95)
left(180)
forward(185)
left(180)
forward(90)
right(90)
forward(100)
left(180)
forward(100)
left(45)
forward(100)
left(180)
forward(200)
left(180)
forward(100)
left(90)
forward(100)
left(180)
forward(200)
#დავასრულე მზის ხატვა

#ვიწყებ პირველი სახლის შენესებას

#ვხატავ ოთკუთხედს
penup()
goto(-250,-150)
pendown()
left(135)

begin_fill()
color("black")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#დავასრულე ოთკუთხედის ხატვა

#ვიწყებ კარის ხატვას
begin_fill()
forward(70)
color("brown")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
#დავასრულე კარის ხატვა

#ვიწყებ სახურავს
penup()
goto(-50,50)
pendown()

color("dark green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#დავასრულე სახურავი

#ვიწყებ ფანჯრებს
penup()
goto(-245,-25)
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
goto(-100,-25)
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
#დავასრულე პირველი სახლი

#ვიწყებ მეორე სახლის შენებას

#ვხატავ ოთხკუთხედს
penup()
goto(0,-150)
pendown()
left(90)

begin_fill()
color("red")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#დავასრულე ოთხკუთხედი

#ვიწყებ კარის ხატვას
begin_fill()
forward(70)
color("purple")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
#დავასრულე კარის ხატვა

#ვიწყებ სახურავს
penup()
goto(200,50)
pendown()

color("antique white")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#დავასრულე სახურავი

#ვიწყებ ფანჯრებს
penup()
goto(10,-25)
pendown()

color("orange")
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
goto(145,-25)
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
#დავასრულე ფანჯრები
#დავასრულე მეორე სახლი

#ვიწყებ მესამე სახლს

#ვიწყებ ოთხკუთხედის ხატვას
penup()
goto(250,-150)
pendown()
left(90)

begin_fill()
color("aqua")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#დავასრულე ოთხკუტხედის ხატვა

#ვიწყებ კარის ხატვას
begin_fill()
forward(70)
color("grey")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
#დავასრულე კარის ხატვა

#ვიწყებ სახურავის ხატვას
penup()
goto(450,50)
pendown()

color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#დავასრულე სახურავის ხატვა

#ვიწყებ ფანჯრების ხატვას
penup()
goto(260,-25)
pendown()

color("yellow")
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
goto(395,-25)
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
#დავასრულე ფანჯრების ხატვა

#დავასრულე მესამე სახლი

#ვიწყებ ეზოს
penup()
goto(0,-150)
pendown()

begin_fill()
color("green")
left(90)
forward(700)
right(90)
forward(300)
right(90)
forward(1250)
right(90)
forward(300)
right(90)
forward(1000)
end_fill()
#დავასრულე ეზოს ხატვა

#ვიწყებ ხის ხატვას
penup()
goto(-500,-250)
pendown()

begin_fill()
color("brown")
left(90)
forward(320)
left(180)
forward(320)
left(90)
forward(55)
left(90)
forward(320)
left(90)
forward(55)
end_fill()

begin_fill()
color("dark green")
penup()
goto(-470,200)
pendown()
circle(100)
end_fill()
#დავასრულე ხის ხატვა

exitonclick()

