import pygame

pygame.init()

LARGURA = 900
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desafio Industrial")

# Cores RGB
CINZA = (100, 100, 100)
AZUL = (40, 100, 180)
VERDE = (30, 160, 80)
BRANCO = (255, 255, 255)

rodando = True


while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Limpa a tela
    tela.fill(CINZA)

    # Desenha o personagem
    pygame.draw.rect(tela, AZUL, (100, 300, 50, 70))#Eixo X; Eixo Y; LArgura ; Altura

    # Desenha uma peça industrial
    pygame.draw.rect(tela, VERDE, (400, 300, 40, 40))

    # Atualiza a janela
    pygame.display.flip()

pygame.quit()