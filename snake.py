from turtle import Turtle
position = [(0, 0), (-15, 0), (-30, 0)]


class Snake:

    def __init__(self):
        self.snake = []
        for i in position:
            joe = Turtle()
            joe.penup()
            joe.shapesize(stretch_wid=.75, stretch_len=.75)
            joe.color("white")
            joe.shape("square")
            joe.goto(i)
            self.snake.append(joe)
        self.head = self.snake[0]

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.head.fd(15)

    def grow(self):
        joe = Turtle()
        joe.penup()
        joe.shapesize(stretch_wid=.75, stretch_len=.75)
        joe.color("white")
        joe.shape("square")
        x = self.snake[-1].xcor()
        y = self.snake[-1].ycor()
        joe.goto(x, y)
        self.snake.append(joe)

    def up(self):
        if self.head.heading() == 0:
            self.head.setheading(90)
        elif self.head.heading() == 180:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 0:
            self.head.setheading(270)
        elif self.head.heading() == 180:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 90:
            self.head.setheading(180)
        elif self.head.heading() == 270:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 90:
            self.head.setheading(0)
        elif self.head.heading() == 270:
            self.head.setheading(0)

    def is_het(self, segment):
        for i in range(2, len(self.snake)):
            if self.snake[i].distance(segment) < 15:
                return True
        return False

    def right_wall(self):
        x = self.head.xcor()*-1
        y = self.head.ycor()
        self.head.goto(x, y)

    def up_wall(self):
        x = self.head.xcor()
        y = self.head.ycor()
        self.head.goto(x, y * -1)

    def up_up(self):
        x = self.head.xcor()
        y = self.head.ycor()
        self.head.goto(x, -275)

