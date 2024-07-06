import pygame as pg

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pg.transform.scale2x(pg.image.load('./assets/images/pipe.png'))
IMAGEM_CHAO = pg.transform.scale2x(pg.image.load('./assets/images/base.png'))
IMAGEM_BACKGROUND = pg.transform.scale2x(pg.image.load('./assets/images/bg.png'))
IMAGENS_PASSARO = [
    pg.transform.scale2x(pg.image.load('./assets/images/bird1.png')),
    pg.transform.scale2x(pg.image.load('./assets/images/bird2.png')),
    pg.transform.scale2x(pg.image.load('./assets/images/bird3.png'))
]

pg.font.init()
FONTE_PONTOS = pg.font.Font('./assets/fonts/flappy-bird-regular.ttf', 70)
FONTE_MSG = pg.font.Font('./assets/fonts/flappy-bird-regular.ttf', 50)
