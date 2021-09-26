import turtle

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# paddel A
paddel_a = turtle.Turtle()
paddel_a.speed(0)
paddel_a.shape("square")
paddel_a.color("blue")
paddel_a.shapesize(stretch_wid=5, stretch_len=1)
paddel_a.penup()
paddel_a.goto(-350, 0)

# paddel B
paddel_b = turtle.Turtle()
paddel_b.speed(0)
paddel_b.shape("square")
paddel_b.color("blue")
paddel_b.shapesize(stretch_wid=5, stretch_len=1)
paddel_b.penup()
paddel_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 290)
pen.write("Player A: 0  Payer B: 0", align="center",font=("Courier", 15, "normal"))

# function


def paddel_a_up():
    y = paddel_a.ycor()
    y += 30
    paddel_a.sety(y)


def paddel_a_dwon():
    y = paddel_a.ycor()
    y -= 30
    paddel_a.sety(y)


def paddel_b_up():
    y = paddel_b.ycor()
    y += 20
    paddel_b.sety(y)


def paddel_b_dwon():
    y = paddel_b.ycor()
    y -= 20
    paddel_b.sety(y)


# keyboarding binding
wn.listen()
wn.onkeypress(paddel_a_up, "w")
wn.onkeypress(paddel_a_dwon, "s")
wn.onkeypress(paddel_b_up, "i")
wn.onkeypress(paddel_b_dwon, "l")


# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # boarder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Payer B: {}".format(score_a, score_b), align="center",font=("Courier", 15, "normal"))

    if ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Payer B: {}".format(score_a, score_b), align="center",font=("Courier", 15, "normal"))

    # paddel and ball collision
    if (ball.xcor() > 345 and ball.xcor() < 350) and (ball.ycor() < paddel_b.ycor() + 40 and ball.ycor() > paddel_b.ycor() - 40):
        ball.setx(345)
        ball.dx *= -1

    if (ball.xcor() < -345 and ball.xcor() < 350) and (ball.ycor() < paddel_a.ycor() + 40 and ball.ycor() > paddel_a.ycor() - 40):
        ball.setx(-345)
        ball.dx *= -1
