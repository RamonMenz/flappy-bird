import pygame as pg

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pg.transform.scale2x(pg.image.load('images/pipe.png'))
IMAGEM_CHAO = pg.transform.scale2x(pg.image.load('images/base.png'))
IMAGEM_BACKGROUND = pg.transform.scale2x(pg.image.load('images/bg.png'))
IMAGENS_PASSARO = [
    pg.transform.scale2x(pg.image.load('images/bird1.png')),
    pg.transform.scale2x(pg.image.load('images/bird2.png')),
    pg.transform.scale2x(pg.image.load('images/bird3.png'))
]

pg.font.init()
FONTE_PONTOS = pg.font.SysFont('arial', 50)
FONTE_MSG = pg.font.SysFont('arial', 25)
