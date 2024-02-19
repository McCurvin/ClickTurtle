import turtle #BY MC CURVIN ROYERAS
myScreen = turtle.getscreen()
myScreen.bgcolor("pink")
pin = turtle.Turtle()
def talk(message, x, y):
    pin.penup()
    pin.goto(x, y)
    pin.pendown()
    pin.pencolor("red")
    pin.write(message, align="center", font=("Arial", 10, "normal"))
    pin.penup()
click = 0
def onClick(x, y):
    global click
    click += 1
    talk(f"You clicked {click} times!", x, y)
    return click

myScreen.onclick(onClick)

talk(f"Click on the screen!", 0, 0)

turtle.mainloop()
