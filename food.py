import random
import pygame


class Food:
    @staticmethod
    def generate_xy():
        x = round(random.randrange(0, 600 - 10) / 10.0) * 10.0
        y = round(random.randrange(0, 400 - 10) / 10.0) * 10.0
        return x, y

    @staticmethod
    def generate_food(display, color, x, y, rand_num):
        if rand_num % 3 == 0:
            return pygame.draw.circle(display, color, (x, y), 5, 0), True
        return pygame.draw.rect(display, color, [x, y, 10, 10]), False
