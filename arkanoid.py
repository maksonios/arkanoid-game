import pgzrun
from pgzero.actor import Actor
import sys

mod = sys.modules['__main__']
import random

WIDTH = 600
HEIGHT = 800

paddle = Actor("paddle.png")
paddle.x = 300
paddle.y = 800

ball = Actor("ball.png")
ball.x = 300
ball.y = 730
ball_x_speed = 7
ball_y_speed = 7

obstacles_list = []


def place_obstacles(x, y, image):
    obstacle_x = x
    obstacle_y = y
    for i in range(8):
        obstacle = Actor(image)
        obstacle.x = obstacle_x
        obstacle.y = obstacle_y
        obstacle_x += 70
        obstacles_list.append(obstacle)


game_over = False
playerLives = 3


def update_ball():
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH) or (ball.x <= 0):
        ball_x_speed *= -1
    if (ball.y >= HEIGHT) or (ball.y <= 0):
        ball_y_speed *= -1


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
    global ball_x_speed, ball_y_speed, game_over, playerLives
    update_ball()
    if paddle.colliderect(ball):
        ball_y_speed *= -1
        rand = random.randint(0, 1)
        if rand:
            ball_x_speed *= -1

    for obstacle in obstacles_list:
        if ball.colliderect(obstacle):
            obstacles_list.remove(obstacle)
            ball_y_speed *= -1
            ball_x_speed *= -1

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
