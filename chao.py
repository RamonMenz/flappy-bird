from config import *


class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x0 = 0
        self.x1 = self.LARGURA

    def mover(self):
        self.x0 -= self.VELOCIDADE
        self.x1 -= self.VELOCIDADE

        if self.x0 + self.LARGURA < 0:
            self.x0 = self.x1 + self.LARGURA
        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x0 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x0, self.y))
        tela.blit(self.IMAGEM, (self.x1, self.y))
