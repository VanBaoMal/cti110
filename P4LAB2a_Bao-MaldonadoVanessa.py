# This program uses turtle to draw a square and triangle
# CTI-110
# P4LAB2a - Shapes
# Vanessa Bao-Maldonado
# June 26, 2022

def main():
    # Import turtle and label screen
    import turtle
    wn = turtle.Screen()
    wn.title("Ethan & Emmett")

    # Create turtle Emmett
    emmett = turtle.Turtle()
    emmett.shape("turtle")
    emmett.pensize(5)

    # Create turtle Ethan
    ethan = turtle.Turtle()      
    ethan.color("blue")
    ethan.pensize(5)
    ethan.shape("turtle")

    # Emmett the turtle draws a square
    for i in range(4):
        emmett.forward(50)
        emmett.left(90)

    # Ethan the turtle draws a triangle
    for j in range(3):
        ethan.forward(80)             
        ethan.left(120)

# Program start
main()
