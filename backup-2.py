import pgzrun
from pgzero.actor import Actor
import sys

mod = sys.modules['__main__']
import random

WIDTH = 600
HEIGHT = 800


class Paddle(Actor):
    def __init__(self):
        super().__init__("paddle.png", (300, 800))
        self.x_speed = 3

    def draw(self):
        return super().draw()


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

    def collide(self, obj: Actor) -> bool:
        if not self.colliderect(obj): return False

        if obj.right >= self.centerx >= obj.left:
            self.y_speed *= -1
            self.update()

        elif obj.bottom >= self.centery >= obj.top:
            self.x_speed *= -1
            self.update()

        else:
            self.y_speed *= -1
            self.x_speed *= -1
            self.update()

        return True


class Obstacle(Actor):
    def __init__(self, image, x, y, hits=1) -> None:
        super().__init__(image, (x, y))
        self.hit = 0
        self.max_hits = hits

    def is_destroyed(self) -> bool:
        self.hit += 1
        if self.hit >= self.max_hits:
            return True

        return False


def place_obstacles(x, y, image, hits):
    for x in range(x, x + 8 * 70, 70):
        obstacles_list.append(Obstacle(image, x, y, hits))


obstacles_list: list[Obstacle] = []

paddle = Paddle()

ball = Ball()

game_over = False
playerLives = 3


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
    global game_over, playerLives
    ball.update()
    ball.collide(paddle)

    for obstacle in obstacles_list:
        if ball.collide(obstacle) and obstacle.is_destroyed():
            obstacles_list.remove(obstacle)

    if ball.y >= HEIGHT and playerLives != 0:
        ball.y = 300
        playerLives -= 1

    if playerLives == 0:
        game_over = True


def on_mouse_move(pos):
    paddle.centerx = pos[0]


place_obstacles(50, 120, "element_green_rectangle_glossy.png", 2)
place_obstacles(50, 200, "ball_obstacle.png", 1)

pgzrun.go()