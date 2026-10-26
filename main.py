import pygame

pygame.init()

LARGURA = 900
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desafio Industrial - a SAGA SENAI NA INDÚISTRIA")

# Cores RGB
CINZA = (100, 100, 100)
AZUL = (40, 100, 180)
VERDE = (30, 160, 80)
BRANCO = (255, 255, 255)

rodando = True

relogio = pygame.time.Clock()

while rodando:
       # Fundo da fábrica
    tela.fill((35, 40, 48))

    # Piso industrial
    pygame.draw.rect(tela, (75, 80, 85), (0, 400, 900, 200))

    # Linhas do piso
    for x in range(0, 900, 100):
        pygame.draw.line(
            tela,
            (110, 115, 120),
            (x, 400),
            (x, 600),
            2
        )

    # Esteira transportadora
    pygame.draw.rect(tela, (25, 25, 25), (250, 320, 450, 60))
    pygame.draw.rect(tela, (130, 130, 130), (250, 320, 450, 5))

    # Personagem
    pygame.draw.rect(tela, (40, 130, 230), (100, 300, 50, 70))

    # Peça para coleta
    pygame.draw.rect(tela, (255, 190, 30), (400, 330, 35, 35))

    # Atualiza a janela
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()