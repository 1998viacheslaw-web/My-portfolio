from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bricks import creating_bricks

bricks = creating_bricks()

screen=Screen()
screen.bgcolor('black')
screen.title('Breakout')
screen.setup(width=1000,height=800)


my_paddle=Paddle()
my_ball=Ball(screen)


count_bricks=0

ball_fell=False

scoreboard=Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(-450,30)
scoreboard.color("white")

count_lives=5

lives=Turtle()
lives.hideturtle()
lives.penup()
lives.goto(-450,60)
lives.color("white")

start_text=Turtle()
start_text.hideturtle()
start_text.penup()
start_text.goto(0,0)
start_text.color("white")
start_text.write('Press SPACE to start',align='center',font=('Arial',30))


def reflection():
    distance=my_ball.distance(my_paddle)
    if distance<=60 and my_ball.dy < 0:
        my_ball.dy=abs(my_ball.dy)

def hit_bricks():
    global count_bricks
    for b in bricks:
        distance = my_ball.distance(b)
        if distance <= 18:
            b.hideturtle()
            bricks.remove(b)
            my_ball.dy = -my_ball.dy
            count_bricks += 1
            scoreboard.clear()
            scoreboard.write(f'Score: {count_bricks}', align='center', font=('Arial', 12))
            if len(bricks) == 0:
                text = Turtle()
                text.hideturtle()
                text.penup()
                text.goto(0, 0)
                text.pendown()
                text.color('white')
                text.write('YOU WIN!', align='center', font=('Arial', 30))
                my_ball.dx = 0
                my_ball.dy = 0
            if count_bricks in (10, 20, 30, 40):
                my_ball.higher_speed()
            break

def falling():
  global count_lives,ball_fell
  y_ball=my_ball.pos()[1]
  if y_ball<=-420 and not ball_fell:
    count_lives-=1
    lives.clear()
    lives.write(f'Lives:{count_lives}', align='center', font=('Arial',12))
    my_paddle.goto(0,-390)
    my_ball.x=my_ball.start_x
    my_ball.y=my_ball.start_y
    my_ball.goto(my_ball.start_x, my_ball.start_y)
    if count_lives<1:
        text=Turtle()
        text.hideturtle()
        text.penup()
        text.goto(0,0)
        text.pendown()
        text.color('white')
        text.write('GAME OVER!', align='center', font=('Arial', 30))
        my_ball.dx = 0
        my_ball.dy = 0
    else:
        ball_fell=False

def start_game():
  start_text.clear()
  my_ball.bouncing_ball()
  game_loop()


screen.listen()
screen.onkey(my_paddle.move_left,'Left')
screen.onkey(my_paddle.move_right,'Right')
screen.onkey(start_game,'space')
screen.onkeypress(my_paddle.move_left,'Left')
screen.onkeypress(my_paddle.move_right,'Right')


def game_loop():
  reflection()
  hit_bricks()
  falling()
  screen.ontimer(game_loop, 20)


screen.mainloop()

