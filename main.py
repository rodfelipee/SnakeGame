import pygame
import time
import random

pygame.init()

# Cores

branco = (255,255,255)
amarelo = (255,255,100)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

# Tela
screenw = 600
screenh = 400

screen = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("Snake Game")

# Velocidade e tempo
relogio = pygame.time.Clock()

bloco_snake = 10
vel_snake = 15

# Fontes
fonte = pygame.font.SysFont("Arial", 25)
fonte_score = pygame.font.SysFont("Arial", 20)

# Score
def game_score(score):
    valor = fonte_score.render("Seu score: " + str(score), True, amarelo)
    screen.blit(valor, [0, 0])

# Snake
def snake(bloco_snake, lista_snake):
    for a in lista_snake:
        pygame.draw.rect(screen, verde, [a[0], a[1], bloco_snake, bloco_snake])

def msg(mensagem, color):
    mensagem = fonte.render(mensagem, True, color)
    screen.blit(mensagem, [screenw / 6, screenh / 3])

# main
def main():
    gameover = False
    gameclose = False

    x1 = screenw / 2
    y1 = screenh / 2

    x1_change = 0
    y1_change = 0
    
    lista_snake = []
    snakesize = 1

    # Food
    foodx = round(random.randrange(0, screenw - bloco_snake) / 10.0) * 10.0
    foody = round(random.randrange(0, screenh - bloco_snake) / 10.0) * 10.0

    while not gameover:
        while gameclose == True:
            screen.fill(preto)
            msg("Você perdeu!\nPressione N para jogar novamente ou Q para sair", vermelho)
            game_score(snakesize = 1)
            pygame.display.update()
        
            # Keypress
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover = True
                        gameclose = False
                    elif event.key == pygame.K_n:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                # Esquerda
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -bloco_snake
                    y1_change = 0
                # Direita
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = bloco_snake
                    y1_change = 0
                # Baixo
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = bloco_snake
                # Cima
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -bloco_snake

        if x1 >= screenw or x1 < 0 or y1 >= screenh or y1 < 0:
            gameclose = True
        x1 += x1_change
        y1 += y1_change

        screen.fill(preto)

        pygame.draw.rect(screen, azul, [foodx, foody, bloco_snake, bloco_snake])
        
        snakehead = []
        snakehead.append(x1)
        snakehead.append(y1)
        lista_snake.append(snakehead)

        if len(lista_snake) > snakesize:
            del lista_snake[0]

        for c in lista_snake[:-1]:
            if c == snakehead:
                gameclose = True
        
        snake(bloco_snake, lista_snake)
        game_score(snakesize - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screenw - bloco_snake) / 10.0) * 10.0
            foody = round(random.randrange(0, screenh - bloco_snake) / 10.0) * 10.0

            snakesize += 1

        relogio.tick(vel_snake)

    pygame.quit()
    quit()

main()

