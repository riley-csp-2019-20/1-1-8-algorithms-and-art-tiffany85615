#create turtle
import turtle as trtl
#draw a snowman
#define variables and set pencolor and pensize
man = trtl.Turtle()
man.speed(0)
man.pensize(5)
man.pencolor("light grey")

#create the ground
man.fillcolor("light grey")
man.begin_fill()
man.penup()
man.goto(300,-200)
man.right(90)
man.pendown()
man.forward(100)
man.right(90)
man.forward(600)
man.right(90)
man.forward(100)
man.right(90)
man.forward(600)
man.end_fill()

#create the sky
man.pencolor("sky blue")
man.fillcolor("sky blue")
man.begin_fill()
man.left(90)
man.forward(500)
man.left(90)
man.forward(600)
man.left(90)
man.forward(500)
man.left(90)
man.forward(600)
man.end_fill()

#create body of snowman
man.pencolor("white")
man.penup()
ycor = -280
man.goto(0,ycor)
radius = 100
num_crcls = 0
while num_crcls < 3:
    man.fillcolor("white")
    man.begin_fill()
    man.circle(radius)
    man.end_fill()
    man.penup()
    ycor = ycor + radius*2 - 5
    radius = radius - 2/5*radius
    man.goto(0, ycor)
    man.pendown()
    num_crcls = num_crcls + 1


#make the eyes
man.color("black")
man.penup()
man.goto(12,62)
man.pendown()
man.dot()
man.penup()
man.goto(-12,62)
man.dot()

#make the nose
man.fillcolor("dark orange")
man.pensize(2)
man.penup()
man.goto(0,55)
man.down()
man.begin_fill()
man.color("dark orange")
man.setheading(340)
man.forward(12)
man.left(160)
man.forward(15)
man.setheading(270)
man.forward(6)
man.end_fill()
#draw buttons
 
man.pensize(5)
man.color("dark red")
man.penup()
man.goto(0,0)
man.pendown()
man.dot()
man.penup()
man.goto(0,-50)
man.down()
man.dot()
 
#draw right arm
man.up()
man.goto(57,0)
man.down()
man.setheading(42)
man.color("brown")
man.pensize(2)
man.forward(60)
man.left(180)
man.forward(30)
man.setheading(80)
man.forward(30)
man.left(180)
man.forward(30)
man.setheading(0)
man.forward(30)
 
#draw left arm
man.up()
man.goto(-57,0)
man.down()
man.setheading(138)
man.forward(60)
man.left(180)
man.forward(30)
man.setheading(100)
man.forward(30)
man.left(180)
man.forward(30)
man.setheading(180)
man.forward(30)
 
#draw rim of hat
man.up()
man.goto(60,90)
man.setheading(180)
man.color("black")
man.down()
man.forward(120)
 
#draw hat
man.up()
man.goto(-40,90)
man.setheading(90)
man.fillcolor("black")
man.begin_fill()
man.forward(60)
man.right(90)
man.forward(80)
man.right(90)
man.forward(60)
man.right(90)
man.forward(80)
man.end_fill()

snowballs = 3
while snowballs > 2:
    man.goto(-170,240)
    man.pensize(7)
    man.pencolor("white")
    man.dot()
    man.up()
    man.goto(150,220)
    man.dot()
    man.up()
    man.goto(110,200)
    man.dot()
    




wn = trtl.Screen()
wn.mainloop()
