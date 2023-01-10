import pgzrun
from pgzero.actor import Actor
import sys

mod = sys.modules['__main__']
import random

WIDTH = 600
HEIGHT = 800

obstacles_list = []


class Paddle(Actor):
    def __init__(self):
        super().__init__("paddle.png", (300, 800))

    def draw(self):
        return super().draw()

    def look_at(self, pos):
        self.x = pos[0]

    def is_collided(self, ball):
        return self.colliderect(ball)


class Ball(Actor):
    def __init__(self):
        super().__init__("ball.png", (300, 730))
        self.y_speed = 7
        self.x_speed = 7

    def update(self):
        self.x -= self.x_speed
        self.y -= self.y_speed
        if (self.x >= WIDTH) or (self.x <= 0):
            self.x_speed *= -1
        if (self.y >= HEIGHT) or (self.y <= 0):
            self.y_speed *= -1

    def draw(self):
        return super().draw()


def place_obstacles(x, y, image):
    for obstacle in range(x, x + 8 * 70, 70):
        obstacles_list.append(Actor(image, (x, y)))


paddle = Paddle()

ball = Ball()

game_over = False
playerLives = 3
points = 0


def draw():
    mod.screen.blit("background-image.jpg", (0, 0))
    paddle.draw()
    ball.draw()
    for obstacle in obstacles_list:
        obstacle.draw()
    if game_over:
        mod.screen.blit("game-over.png", (0, 0))
    if playerLives == 3:
        mod.screen.blit("heart_3.png", (0, 0))
    if playerLives == 2:
        mod.screen.blit("heart_2.png", (0, 0))
    if playerLives == 1:
        mod.screen.blit("heart_1.png", (0, 0))


def update():
    global game_over, playerLives, points
    ball.update()
    if paddle.colliderect(ball):
        ball.y_speed *= -1
        rand = random.randint(0, 1)
        if rand:
            ball.x_speed *= -1

    for obstacle in obstacles_list:
        if ball.colliderect(obstacle):
            obstacles_list.remove(obstacle)
            ball.y_speed *= -1
            ball.x_speed *= -1
            points += 1

    if ball.y >= HEIGHT and playerLives != 0:
        ball.y = 300
        playerLives -= 1

    if playerLives == 0:
        game_over = True


def on_mouse_move(pos):
    paddle.pos = (pos[0], paddle.pos[1])


coloured_box_list = ["element_green_rectangle_glossy.png", "ball_obstacle.png"]
x = 50
y = 120
for coloured_box in coloured_box_list:
    place_obstacles(x, y, coloured_box)
    y += 80

pgzrun.go()