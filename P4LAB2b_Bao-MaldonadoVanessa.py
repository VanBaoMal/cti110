# This program uses turtle to draw my initials
# CTI-110
# P4LAB2b - Initials
# Vanessa Bao-Maldonado
# June 26, 2022

def main():
    # Import turtle and label screen
    import turtle
    wn = turtle.Screen()
    wn.title("My Initials: VM")

    # Create turtle
    name = turtle.Turtle()
    name.pensize(5)
    name.color("hotpink")

     # This draws the letter V
    for j in range(2):
        name.left(240)
        name.forward(80) 

    # Move location for next initial
    name.penup()
    name.left(240)
    name.forward(150)
    name.left(240)
    name.pendown()
        
    # This draws half the letter M
    for i in range(2):
        for k in range(1):
            name.forward(80)
            name.penup()
            name.left(180)
            name.forward(80)
            name.left(240)
            name.pendown()

    #move to correct position
    name.penup()
    name.left(0)
    name.forward(80)
    name.left(240)
    name.pendown()

    # This draws half the letter M
    for i in range(2):
        for k in range(1):
            name.forward(80)
            name.penup()
            name.left(180)
            name.forward(80)
            name.left(240)
            name.pendown()
    

    wn.mainloop()          

# Program start
main()
