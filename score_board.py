from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.build_bord()

    def build_bord(self):
        self.clear()
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(0, 330)
        self.color("white")
        self.write(f"score: {self.score}", False, "center",  ('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game over", False, "center", ('Arial', 30, 'normal'))

    def increase_score(self):
        self.score += 1
