from turtle import *
import turtle

#we want to paint a house


#step 1:   draw a square
speed(5)
width(7)
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

#drawing a door
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
#end



#roof
penup()
goto(200,200)
pendown()
color("red")
right(120)
forward(115)
left(60)
forward(115)
#end

#window1
penup()
goto(80,220)
pendown()
color("brown")
begin_fill()
left(60)

left(180)
forward(15)
right(90)
forward(30)
right(90)
forward(15)
right(90)
forward(11)

right(10)
forward(20)
right(70)
end_fill()

#left window
penup()
goto(20,70)
pendown()
color("green")
begin_fill()
right(10)
forward(40)
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
end_fill()
#end

#right window

penup()
goto(150, 70)
right(80)
pendown()
color("blue")
begin_fill()
right(10)
forward(40)
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
end_fill()

exitonclick()