import pygame


class Tela:
    largura = 600
    altura = 400

    def __init__(self):
        self.x = 300
        self.y = 200
        self.x_change = 0
        self.y_change = 0

    @staticmethod
    def display():
        return pygame.display.set_mode((Tela.largura, Tela.altura))

    @staticmethod
    def game_close(x, y):
        if x >= Tela.largura or x < 0 or y > Tela.altura or y < 0:
            return True
        return False
