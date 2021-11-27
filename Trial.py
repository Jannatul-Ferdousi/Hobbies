import turtle
wn = turtle.Screen()
wn.bgcolor('sky blue')
wn.title("Happy Birthday")
turtle.color("Blue") #to make jui blue
style=("moon",'30','italic','underline', 'bold')
turtle.write("JUI", font= style, align='right')

s = turtle.Turtle()
#s.forward(50)

#square
for i in range(4):
    s.forward(50)
    s.right(90)

# star
for i in range(5):
    s.forward(50)
    s.right(144)


turtle.done()