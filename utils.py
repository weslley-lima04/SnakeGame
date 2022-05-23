from screen import Tela
import pygame
import sys
from main import loop


class Utils:
    def __init__(self):
        self.game_over = False
        self.game_close = False

    @staticmethod
    def message(msg, cor):
        mesg = pygame.font.SysFont(None, 20).render(msg, True, cor)
        dis = Tela.display()
        dis.blit(mesg, [(Tela.largura / 5), (Tela.altura / 3)])

    @staticmethod
    def end_game(score):
        while True:
            # Tela.display(Tela.largura, Tela.altura).fill(255, 255, 255)
            Utils.message(f"Você perdeu! Aperte C para jogar novamente ou Q para sair. Pontos: {score}",
                          (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit(0)
                    if event.key == pygame.K_c:
                        loop()
            pygame.display.update()
