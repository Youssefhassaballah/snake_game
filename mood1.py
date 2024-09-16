from wall import Wall
from snake import Snake
import time
from turtle import Screen
from food import Food
from score_board import Board
##############################


def play():

    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=900, height=800)
    screen.title("joe's snake game")
    screen.tracer(0)
    screen.listen()
    snake = Snake()
    board = Board()
    wall = Wall(590, 590)
    ##############################
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(snake.left, "Left")
    food = Food()
    ##############################
    end_game = False
    while not end_game:
        screen.update()
        if snake.is_het(snake.snake[0]):
            end_game = True
        if snake.head.xcor() > 275:
            snake.right_wall()
        elif snake.head.xcor() < -275:
            snake.right_wall()
        if snake.head.ycor() > 275:
            snake.up_up()
        if snake.head.ycor() < -275:
            snake.up_wall()
        board.build_bord()
        time.sleep(.05)
        snake.move()
        if food.distance(snake.snake[0]) < 15:
            food.refresh()
            snake.grow()
            board.increase_score()

    board.game_over()
    screen.exitonclick()


play()

