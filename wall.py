from turtle import Turtle


class Wall(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.color("green")
        self.width(5)
        self.goto(-(width/2), -(height/2))
        self.pendown()
        self.forward(width)
        self.left(90)
        self.forward(height)
        self.left(90)
        self.forward(width)
        self.left(90)
        self.forward(height)
