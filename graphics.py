'''
    Andres Schuchert
    CS 5001 
    November 18, 2018
'''
import turtle

SQUARE = 50

turtle.speed(0)
turtle.hideturtle()

def keep_board_open():
    turtle.mainloop()

def draw_board(n):
    ''' 
    Function: draw_board
    Parameters: n, an int for # of squares
    Returns: nothing
    Does: Draws an nxn board with a green background
    '''

    turtle.setup(n * SQUARE + SQUARE, n * SQUARE + SQUARE)
    turtle.screensize(n * SQUARE, n * SQUARE)
    turtle.bgcolor('white')

    # Create the turtle to draw the board
    othello = turtle.Turtle()
    othello.penup()
    othello.speed(0)
    othello.hideturtle()
    #Line color is black, fill color is green
    othello.color("black", "forest green")
    
    # Move the turtle to the upper left corner
    corner = -n * SQUARE / 2
    othello.setposition(corner, corner)
  
    # Draw the green background
    othello.begin_fill()
    for i in range(4):
        othello.pendown()
        othello.forward(SQUARE * n)
        othello.left(90)
    othello.end_fill()

    # Draw the horizontal lines
    for i in range(n + 1):
        othello.setposition(corner, SQUARE * i + corner)
        draw_lines(othello, n)

    # Draw the vertical lines
    othello.left(90)
    for i in range(n + 1):
        othello.setposition(SQUARE * i + corner, corner)
        draw_lines(othello, n)

def draw_lines(turt, n):
    turt.pendown()
    turt.forward(SQUARE * n)
    turt.penup()

def draw_stone(point, color="black"):
    '''
    Function name: draw_stone
    Parameters: list, string
    Return: None
    '''
    turtle.penup()
    turtle.goto(point[0],point[1])
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

def screen_goto(x,y):
    '''
    Go to a specific point
    '''
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def screen_click(function):
    turtle.onscreenclick(function)
