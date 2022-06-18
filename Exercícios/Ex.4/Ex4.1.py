import turtle

bob = turtle.Turtle()
print(bob)
bob.speed(5)
bob.pu()
bob.backward(100)
bob.pd()
#triangle
for i in range(3):
    bob.forward(100)
    bob.left(120)

bob.pu()
bob.fd(50)
bob.pd()

#circle
bob.circle(100)
bob.pu()
bob.backward(100)
bob.pd()

#square
for i in range(4):
    bob.forward(200)
    bob.left(90)

turtle.mainloop()

