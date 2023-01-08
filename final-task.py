import pgzrun
from pgzero.actor import Actor
import sys

mod = sys.modules['__main__']
import random


class Paddle:
    def __init__(self):
        self.actor = Actor("paddle.png")
        self.actor.x = 300
        self.actor.y = 800

    def draw(self):
        self.actor.draw()

    def look_at(self, pos):
        self.actor.x = pos[0]

    def is_collided(self, ball):
        return self.actor.colliderect(ball)


class Ball:
    def __init__(self):
        self.y_speed = 7
        self.x_speed = 7
        self.actor = Actor("ball.png")
        self.actor.x = 300
        self.actor.y = 730


    def draw(self):
        self.actor.draw()




WIDTH = 600
HEIGHT = 800

paddle = Paddle()
ball = Ball()


def draw():
    mod.screen.blit("background-image.jpg", (0, 0))
    paddle.draw()
    ball.draw()


def update():
    if paddle.is_collided(ball):
        ball.y_speed *= -1
        rand = random.randint(0, 1)
        if rand:
            ball.x_speed *= -1



def on_mouse_move(pos):
    paddle.look_at(pos)


pgzrun.go()
