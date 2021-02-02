from turtle import Turtle
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        pos = 0
        for _ in range(0, 3):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.setx(pos)
            self.snake.append(tim)
            pos -= 20

    def move(self):
        for n in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[n-1].xcor()
            new_y = self.snake[n-1].ycor()
            self.snake[n].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)