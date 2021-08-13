import turtle
import random

'''
Random position of snowflakes
 The number of snowflakes is random between [2,10]
 Random size of snowflakes
'''


# Draw Koch curves recursively, controlling the order and angle
def koch(size, n):
    """Function koch uses recursive thinking to draw a section of N-order curve"""
    if n == 0:
        turtle.fd(size)  # Recursive base example, 0-degree curve is a straight line
        print("N==0")
    else:
        for i in [0, 60, -120, 60]:
            turtle.left(i)
            koch(size / 3, n - 1)


def main():
    """Define the main function to call koch"""
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-250, 100)
    turtle.pendown()
    turtle.pensize(2)

    n = 3

    for i in range(0, 3):
        koch(20, 3)
        turtle.right(120)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
   main()