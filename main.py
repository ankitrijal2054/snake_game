from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

pos = 0
snake = []

for _ in range(0,3):
    tim = Turtle(shape = "square")
    tim.color("white")
    tim.setx(pos)
    snake.append(tim)
    pos -= 20








screen.exitonclick()