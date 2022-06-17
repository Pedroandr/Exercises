import turtle

bob = turtle.Turtle()
bob.speed(0)
print(bob)

def polygon(sides):
    for i in range(sides):
        bob.fd(20)
        bob.lt(360/sides)

polygon(60)

turtle.mainloop()