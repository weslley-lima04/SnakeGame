import random


class Cores:
    yellow = (255, 255, 102)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)

    @staticmethod
    def random_color():
        rand_color = tuple((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        return rand_color
