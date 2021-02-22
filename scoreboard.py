from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.score = 0
        #self.high_score = 0
        self.display()
        self.play_again = True

    def display(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score} High Score: {self.read_file()}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display()

    def check_high_score(self):
        if self.score > int(self.read_file()):
            self.write_file(self.score)

    def reset_game(self):
        self.check_high_score()
        self.score = 0
        self.display()

    def read_file(self):
        with open("highscore.txt") as file:
            return file.read()

    def write_file(self,score):
        with open("highscore.txt", mode='w') as file:
            file.write(str(score))
