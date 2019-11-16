# snake game

import turtle
import time
import random

delay = 0.1

# score checker
score_value = 0

# setup the screen
window = turtle.Screen()
window.title('Snake Game by Knyght')
window.bgcolor('black')
window.setup(width=600, height=600)
# turns off the screen updates
window.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('red')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# snake food

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('green')
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# snake body
segments = []


# functions


def move():
    if head.direction == 'up':
        new_y = head.ycor()
        head.sety(new_y + 20)
    if head.direction == 'down':
        new_y = head.ycor()
        head.sety(new_y - 20)
    if head.direction == 'right':
        new_x = head.xcor()
        head.setx(new_x + 20)
    if head.direction == 'left':
        new_x = head.xcor()
        head.setx(new_x - 20)


def go_up():
    if head.direction != 'down':
        head.direction = 'up'


def go_down():
    if head.direction != 'up':
        head.direction = 'down'


def go_left():
    if head.direction != 'right':
        head.direction = 'left'


def go_right():
    if head.direction != 'left':
        head.direction = 'right'


def quit_game():
    window.bye()


# keyboard bindings

window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
window.onkeypress(quit_game, "q")

# pen

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align='center', font=('courier', 24, 'normal'))

# main game loop
while True:
    window.update()

    # check for collisions with borders
    # no borders for this
    # since it is reminiscent of
    # the Nokia Snake Game

    if head.ycor() > 290:
        x = head.xcor()
        y = -290
        head.goto(x, y)
    if head.ycor() < -290:
        x = head.xcor()
        y = 290
        head.goto(x, y)
    if head.xcor() < -290:
        y = head.ycor()
        x = 290
        head.goto(x, y)
    if head.xcor() > 290:
        y = head.ycor()
        x = -290
        head.goto(x, y)

    # eating food (collision check)
    if head.distance(food) < 20:
        # move the food to a new random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color('orange')
        new_segment.penup()
        segments.append(new_segment)

        # update score
        score_value += 1
        pen.clear()
        pen.write("Score: {}".format(score_value), align='center', font=('courier', 24, 'normal'))

    # move the end segments in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move the segment zero to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # collisions of the snake
    # with the snake body
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            pen.clear()
            pen.write("Game Over! Final Score: {}".format(score_value), align="center", font=('courier', 24, 'normal'))

            # hide the segments
            for i in segments:
                i.goto(1000, 1000)

            segments.clear()

            # reset the score
            score_value = 0

    time.sleep(delay)

window.mainloop()
