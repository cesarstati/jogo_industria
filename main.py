import pygame

pygame.init()

LARGURA = 900
ALTURA = 600

tela = pygame.display.set_mode((LARGURA,ALTURA))

pygame.display.set_caption("Desafio Industrial")

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

pygame.quit()