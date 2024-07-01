from passaro import Passaro
from cano import Cano
from chao import Chao
from desenhar_tela import desenhar_tela
from config import *


def main():
    passaros = [Passaro(230, 350)]
    canos = [Cano(700)]
    chao = Chao(730)
    tela = pg.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pg.time.Clock()
    start = False

    while True:
        relogio.tick(30)

        # Interação com o usuário
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_SPACE:
                    start = True
                    for passaro in passaros:
                        passaro.pular()
                if evento.key == pg.K_x:
                    print(f"Pontuação: {pontos}")
                    pg.quit()
                    quit()
                if evento.key == pg.K_r:
                    print(f"Pontuação: {pontos}")
                    main()

        if start:
            # Movimentações
            for passaro in passaros:
                passaro.mover()
            chao.mover()

            adicionar_cano = False
            remover_canos = 0
            for cano in canos:
                for i, passaro in enumerate(passaros):
                    if cano.colidir(passaro):
                        passaros.pop(i)
                    if not cano.passou and passaro.x > cano.x:
                        cano.passou = True
                        adicionar_cano = True
                cano.mover()
                if cano.x + cano.CANO_TOPO.get_width() < 0:
                    remover_canos += 1

            if adicionar_cano:
                pontos += 1
                canos.append(Cano(600))
            if remover_canos > 0:
                remover_canos -= 1
                canos.pop(remover_canos)

            for i, passaro in enumerate(passaros):
                if passaro.y + passaro.imagem.get_height() > chao.y or passaro.y < 0:
                    passaros.pop(i)

        desenhar_tela(passaros, canos, chao, tela, pontos, start)


if __name__ == '__main__':
    main()
