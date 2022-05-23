import pygame


class Snake:
    block = 10

    def __init__(self):
        self.speed = 10
        self.size = 1
        self.lista = []
        self.head = []  # está causando problemas
        self.score = 0

    @staticmethod
    def cobra(tela, lista):
        for i in lista:
            pygame.draw.rect(tela, (0, 0, 0), [i[0], i[1], 10, 10])

    @staticmethod
    def comer(x_tela, y_tela, x_comida, y_comida):
        if x_tela == x_comida and y_tela == y_comida:
            return True
