import pygame

pygame.init()

LARGURA = 900
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desafio Industrial")

CINZA = (100, 100, 100)
AZUL = (40, 100, 180)
VERDE = (30, 160, 80)
PRETO = (25, 25, 25)

jogador_x = 100
jogador_y = 300
velocidade = 5

relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 32)
fonte_pequena = pygame.font.SysFont("Arial", 22)
rodando = True

while rodando:

    # 1. Processa os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jogador_x -= velocidade

    if teclas[pygame.K_RIGHT]:
        jogador_x += velocidade

    if teclas[pygame.K_UP]:
        jogador_y -= velocidade

    if teclas[pygame.K_DOWN]:
        jogador_y += velocidade

    # 2. Desenha o fundo
    tela.fill(CINZA)

    # 3. Desenha os elementos da fábrica
    pygame.draw.rect(tela, CINZA, (0, 400, 900, 200))
    pygame.draw.rect(tela, PRETO, (250, 320, 450, 60))
    pygame.draw.rect(tela, AZUL, (100, 300, 50, 70))
    pygame.draw.rect(tela, VERDE, (400, 330, 35, 35))

    # Título do jogo
    titulo = fonte.render("Factory Top", True, (255, 255, 0))
    tela.blit(titulo, (250, 20))

    # Identificação dos elementos
    texto_esteira = fonte_pequena.render("Esteira", True, (255, 255, 255))
    tela.blit(texto_esteira, (250, 290))

    texto_peca = fonte_pequena.render("Peca", True, (255, 255, 255))
    tela.blit(texto_peca, (395, 370))

    # 4. Atualiza a tela DEPOIS de desenhar tudo
    pygame.display.flip()

    # 5. Limita a velocidade do loop
    relogio.tick(60)

pygame.quit()