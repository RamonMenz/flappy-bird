from config import *


def desenhar_tela(passaros, canos, chao, tela, pontos, start):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    texto = FONTE_PONTOS.render(f'{pontos}', 1, (255, 255, 255))
    tela.blit(texto, ((TELA_LARGURA - texto.get_width()) / 2, 150))

    if not start:
        comecar = FONTE_MSG.render('Press SPACE to start', 1, (255, 255, 255))
        tela.blit(comecar, ((TELA_LARGURA - comecar.get_width()) / 2, TELA_ALTURA / 2))

    if len(passaros) == 0:
        recomecar = FONTE_MSG.render('Press R to restart', 1, (255, 255, 255))
        tela.blit(recomecar, ((TELA_LARGURA - recomecar.get_width()) / 2, TELA_ALTURA / 2))

    chao.desenhar(tela)
    pg.display.update()
