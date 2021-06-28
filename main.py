def ball_angle_randomizer():
    angle = random.random()*math.pi*2
    if angle>math.pi/3 and angle<(math.pi/3)*2:
        angle-=math.pi/3
    elif angle>(math.pi)*4 and angle<(math.pi*5):
        angle-=math.pi/3
    return angle

import pyglet
from pyglet.window import key
import math
import time
import random
window = pyglet.window.Window(800,600, caption='Pong')

left_paddle_x = 50
left_paddle_y = 200
right_paddle_x = 725
right_paddle_y = 200
move_speed = 50

ball = pyglet.sprite.Sprite(pyglet.image.load('ball.png'))
ball.x, ball.y = 400,300
ball_speed = 300.0
ball.dx = ball_speed
ball.dy = ball_speed
ball_angle = ball_angle_randomizer()

left_score = 0
right_score = 0

game_over = False
fps_display = pyglet.window.FPSDisplay(window=window)

@window.event
def on_draw():
    window.clear()
    fps_display.draw()
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                         ('v2f', (window.width//2, window.height-10,
                                  window.width//2,10)))
    left_paddle = pyglet.shapes.Rectangle(x=left_paddle_x, y=left_paddle_y,
                                          width=25, height=200, color=(55, 55, 255))
    right_paddle = pyglet.shapes.Rectangle(x=right_paddle_x, y=right_paddle_y,
                                           width=25, height=200, color=(255, 55, 55))
    left_label = pyglet.text.Label(f'{left_score}',
                                    font_name='Times New Roman',
                                    font_size=36,
                                    x=window.width//2-20, y=window.height-50,
                                    anchor_x='center', anchor_y='center')
    right_label = pyglet.text.Label(f'{right_score}',
                                   font_name='Times New Roman',
                                   font_size=36,
                                   x=window.width // 2 + 20, y=window.height - 50,
                                   anchor_x='center', anchor_y='center')
    left_paddle.draw()
    right_paddle.draw()
    left_label.draw()
    right_label.draw()
    ball.draw()


@window.event
def on_key_press(symbol, modifiers):
    global left_paddle_y, left_paddle_x, right_paddle_y, right_paddle_x
    if symbol == key.W:
        if left_paddle_y <= 325:
            left_paddle_y += move_speed
    elif symbol == key.S:
        if left_paddle_y >= 100:
            left_paddle_y -= move_speed
    elif symbol == key.UP:
        if right_paddle_y <= 325:
            right_paddle_y += move_speed
    elif symbol == key.DOWN:
        if right_paddle_y >= 100:
            right_paddle_y -= move_speed

def update(dt):
    global ball_speed, ball_angle, left_paddle_y, left_score, right_score
    if ball.y>=580 or ball.y<=0:
        ball_angle -= 2*ball_angle
    elif ball.x<=85 and ball.x>=50 and ball.y>=left_paddle_y and ball.y<=left_paddle_y+200:
        ball_angle += 2*(math.pi/2-ball_angle)
        #ball.x+=12.5
    elif ball.x>=700 and ball.x<=750 and ball.y>=right_paddle_y and ball.y<=right_paddle_y+200:
        ball_angle += 2*(math.pi/2-ball_angle)
        #ball.x-=12.5
    if ball.x<=10:
        right_score +=1
        ball.x, ball.y = 400, 300
        ball_angle = ball_angle_randomizer()
        time.sleep(0)
    elif ball.x >=800:
        left_score +=1
        ball.x, ball.y = 400, 300
        ball_angle = ball_angle_randomizer()
        time.sleep(0)
    ball.x += ball.dx * dt * math.cos(ball_angle)
    ball.y += ball.dy * dt * math.sin(ball_angle)
    ball_speed += 1*dt

pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz
pyglet.app.run()