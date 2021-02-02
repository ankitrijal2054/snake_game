from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

pos = 0
snake = []

for _ in range(0,3):
    tim = Turtle(shape = "square")
    tim.color("white")
    tim.penup()
    tim.setx(pos)
    tim.speed("slowest")
    snake.append(tim)
    pos -= 20

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for n in range(len(snake)-1, 0, -1):
        new_x = snake[n-1].xcor()
        new_y = snake[n-1].ycor()
        snake[n].goto(new_x, new_y)
    snake[0].forward(20)






screen.exitonclick()