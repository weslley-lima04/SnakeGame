def loop():
    import sys
    import random
    import pygame
    from colors import Cores
    from screen import Tela
    from utils import Utils
    from food import Food
    from snake import Snake
    tela = Tela.display()
    dis = Tela()
    ut = Utils()
    snk = Snake()
    num_al = random.randint(1, 10)
    rand_color = Cores.random_color()

    fd_x, fd_y = Food.generate_xy()
    pygame.init()

    pygame.display.set_caption("Meu primeiro game!")
    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dis.x_change = -snk.block
                    dis.y_change = 0
                elif event.key == pygame.K_RIGHT:
                    dis.x_change = snk.block
                    dis.y_change = 0
                elif event.key == pygame.K_UP:
                    dis.x_change = 0
                    dis.y_change = -snk.block
                elif event.key == pygame.K_DOWN:
                    dis.x_change = 0
                    dis.y_change = snk.block

        ut.game_close = Tela.game_close(dis.x, dis.y)
        if ut.game_close:
            Utils.end_game(snk.score)

        dis.x += dis.x_change
        dis.y += dis.y_change
        tela.fill(Cores.white)

        special_food = Cores.random_color()
        special_speed = 0

        if num_al == 7:
            special_speed = random.randint(10, 20)
            rand_color = special_food

        food, is_circle = Food.generate_food(tela, rand_color, fd_x, fd_y, num_al)

        snake_head = []  # essa variável está causando problemas
        snake_head.append(dis.x)
        snake_head.append(dis.y)
        snk.lista.append(snake_head)

        if len(snk.lista) > snk.size:
            del (snk.lista[0])

        for j in snk.lista[:-1]:
            if j == snake_head:
                ut.game_close == True

        Snake.cobra(tela, snk.lista)

        pygame.display.update()

        if Snake.comer(dis.x, dis.y, fd_x, fd_y):
            snk.score += 10
            rand_color = Cores.random_color()
            fd_x, fd_y = Food.generate_xy()
            if is_circle:
                snk.speed = 5 if (snk.speed - 2) < 5 else snk.speed - 2
            elif num_al == 7:
                snk.speed += special_speed
            else:
                snk.size += 1
                snk.speed += 1

            num_al = random.randint(1, 10)

        clock.tick(snk.speed)

    pygame.quit()
    quit()


if __name__ == "__main__":
    loop()
