import turtle
import ctypes
user32 = ctypes.windll.user32

#Determine User Screen Size
screenMetrics = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1);
#Screen Setup
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
width=screenMetrics[0]
height=screenMetrics[1]
wn.setup(width, height);
wn.tracer(0)

#PaddleA
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
scale_factor = 20
paddleA_width = width / (75 * scale_factor)
paddleA_height = height / (8 * scale_factor)
paddleA_width=round(paddleA_width)
paddleA_height=round(paddleA_height)
paddleA.shapesize(stretch_wid=paddleA_height, stretch_len=paddleA_width)
paddleA.penup()
paddleA.goto(width/-2.2, 0)
#PaddleB
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
scale_factor = 20
paddleB_width = paddleA_width
paddleB_height = paddleA_height
paddleB.shapesize(stretch_wid=paddleB_height, stretch_len=paddleB_width)
paddleB.penup()
paddleB.goto(width/2.2, 0)
#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball_scale_factor = 40
ball_size = min(width, height) / (30 * ball_scale_factor)
ball.shapesize(stretch_wid=ball_size, stretch_len=ball_size)
ball.goto(0,0)
ball_speed_scale_factor = 1.1
ball_speed = min(width, height) / (30 * ball_scale_factor) * ball_speed_scale_factor
ball.dx = ball_speed_scale_factor * ball_speed
ball.dy = ball_speed_scale_factor * ball_speed


#Function
def paddleAUp(): 
    y = paddleA.ycor()
    y+=20
    paddleA.sety(y)
def paddleADown(): 
    y = paddleA.ycor()
    y-=20
    paddleA.sety(y)
def paddleBUp(): 
    y = paddleB.ycor()
    y+=20
    paddleB.sety(y)
def paddleBDown(): 
    y = paddleB.ycor()
    y-=20
    paddleB.sety(y)
#Keyboard bindings
wn.listen()
wn.onkeypress(paddleAUp, "w")
wn.onkeypress(paddleADown, "s")
wn.onkeypress(paddleBUp, "Up")
wn.onkeypress(paddleBDown, "Down")
#Main Game Loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Points
    score_a = 0
    score_b = 0
    score = turtle.Turtle()
    score.speed(0)
    score.color("white")
    score.penup()
    score.hideturtle()
    score.goto(0, height/2 - 50)

    # update the initial score
    score.clear()
    score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # game loop
    while True:
        wn.update()

        # move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > height/2-ball_size:
            print("Ball hit the top of the screen")
            ball.sety(height/2-ball_size)
            ball.dy *= -1 * ball_speed_scale_factor
        if ball.ycor() < (height/-2)+ball_size:
            print("Ball hit the bottom of the screen")
            ball.sety((height/-2)+ball_size)
            ball.dy *= -1 * ball_speed_scale_factor
        if ball.xcor() > width/2-ball_size:
            ball.goto(0,0)
            score_a += 1
            score.clear()
            score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball.dx *= -1 * ball_speed_scale_factor
        if ball.xcor() < (width/-2)+ball_size:
            ball.goto(0,0)
            score_b += 1
            score.clear()
            score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball.dx *= -1 * ball_speed_scale_factor
        #paddle and ball collisions
        