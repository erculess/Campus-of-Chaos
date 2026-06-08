import pygame
import sys
from config import *
from fighter import Lutador

pygame.init()
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Campus of Chaos - MVP")
RELOGIO = pygame.time.Clock()

# ==========================================
# FUNÇÕES DA INTERFACE
# ==========================================
def desenhar_texto_centralizado(texto, fonte, cor, y_offset=0):
    superficie_texto = fonte.render(texto, True, cor)
    rect_texto = superficie_texto.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 + y_offset))
    TELA.blit(superficie_texto, rect_texto)

def desenhar_barras_vida(hp_p1, hp_p2):
    pygame.draw.rect(TELA, VERMELHO, (50, 30, 400, 30))
    pygame.draw.rect(TELA, VERMELHO, (550, 30, 400, 30))
    
    pygame.draw.rect(TELA, VERDE_IFRN, (50, 30, 400 * (hp_p1 / 100), 30))
    largura_p2 = 400 * (hp_p2 / 100)
    pygame.draw.rect(TELA, VERDE_IFRN, (550 + (400 - largura_p2), 30, largura_p2, 30))

# ==========================================
# LOOP PRINCIPAL DO JOGO
# ==========================================
def main():
    # Estados do Jogo: 'MENU', 'CREDITOS', 'JOGANDO', 'FIM_DE_JOGO'
    estado_jogo = 'MENU'
    opcao_selecionada = 0
    opcoes_menu = ["Jogar", "Créditos", "Sair"]
    mensagem_vitoria = ""

    # Dicionários de controles
    controles_p1 = {
        'esquerda': pygame.K_a, 'direita': pygame.K_d, 'pulo': pygame.K_w,
        'agachar': pygame.K_s, 'soco_fraco': pygame.K_j, 'soco_forte': pygame.K_k, 'defesa': pygame.K_SPACE
    }
    controles_p2 = {
        'esquerda': pygame.K_LEFT, 'direita': pygame.K_RIGHT, 'pulo': pygame.K_UP,
        'agachar': pygame.K_DOWN, 'soco_fraco': pygame.K_o, 'soco_forte': pygame.K_p, 'defesa': pygame.K_l
    }
    
    jogador1 = Lutador(200, CHAO_Y - 120, AZUL, controles_p1)
    jogador2 = Lutador(700, CHAO_Y - 120, CINZA, controles_p2) 
    jogador2.olhando_direita = False

    rodando = True
    while rodando:
        RELOGIO.tick(FPS)
        
        # 1. GERENCIAMENTO DE EVENTOS
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            # Navegação nos Menus (Usamos evento KEYDOWN para ler apenas 1 clique por vez)
            if evento.type == pygame.KEYDOWN:
                if estado_jogo == 'MENU':
                    if evento.key == pygame.K_UP:
                        opcao_selecionada = (opcao_selecionada - 1) % len(opcoes_menu)
                    elif evento.key == pygame.K_DOWN:
                        opcao_selecionada = (opcao_selecionada + 1) % len(opcoes_menu)
                    elif evento.key == pygame.K_RETURN:
                        if opcao_selecionada == 0:
                            estado_jogo = 'JOGANDO'
                        elif opcao_selecionada == 1:
                            estado_jogo = 'CREDITOS'
                        elif opcao_selecionada == 2:
                            rodando = False
                
                elif estado_jogo == 'CREDITOS':
                    if evento.key == pygame.K_ESCAPE or evento.key == pygame.K_RETURN:
                        estado_jogo = 'MENU'

                elif estado_jogo == 'FIM_DE_JOGO':
                    if evento.key == pygame.K_RETURN:
                        # Reinicia os lutadores e volta para a luta
                        jogador1 = Lutador(200, CHAO_Y - 120, AZUL, controles_p1)
                        jogador2 = Lutador(700, CHAO_Y - 120, CINZA, controles_p2)
                        jogador2.olhando_direita = False
                        estado_jogo = 'JOGANDO'
                    elif evento.key == pygame.K_ESCAPE:
                        # Volta para o menu principal
                        jogador1 = Lutador(200, CHAO_Y - 120, AZUL, controles_p1)
                        jogador2 = Lutador(700, CHAO_Y - 120, CINZA, controles_p2)
                        jogador2.olhando_direita = False
                        estado_jogo = 'MENU'

        # 2. LÓGICA E RENDERIZAÇÃO POR ESTADO
        TELA.fill(BRANCO)

        if estado_jogo == 'MENU':
            desenhar_texto_centralizado("CAMPUS OF CHAOS", FONTE_TITULO, VERDE_IFRN, -150)
            
            # Renderiza as opções do menu
            for i, opcao in enumerate(opcoes_menu):
                cor = VERDE_IFRN if i == opcao_selecionada else PRETO
                prefixo = "> " if i == opcao_selecionada else ""
                desenhar_texto_centralizado(f"{prefixo}{opcao}", FONTE_MENU, cor, -20 + (i * 60))
        
        elif estado_jogo == 'CREDITOS':
            desenhar_texto_centralizado("CRÉDITOS", FONTE_TITULO, VERDE_IFRN, -150)
            desenhar_texto_centralizado("Projeto Desenvolvido por:", FONTE_SUBTITULO, PRETO, -50)
            desenhar_texto_centralizado("Emanoelle", FONTE_CREDITOS, PRETO, 10)
            desenhar_texto_centralizado("Ércules", FONTE_CREDITOS, PRETO, 50)
            desenhar_texto_centralizado("Rayanne", FONTE_CREDITOS, PRETO, 90)
            desenhar_texto_centralizado("Pressione ESC para voltar", FONTE_CREDITOS, CINZA, 200)

        elif estado_jogo == 'JOGANDO' or estado_jogo == 'FIM_DE_JOGO':
            # Fundo e Linha do chão
            pygame.draw.line(TELA, PRETO, (0, CHAO_Y), (LARGURA_TELA, CHAO_Y), 5)
            
            if estado_jogo == 'JOGANDO':
                teclas_pressionadas = pygame.key.get_pressed()
                
                jogador1.mover(LARGURA_TELA, CHAO_Y, jogador2)
                jogador1.atacar(teclas_pressionadas, jogador2)
                
                jogador2.mover(LARGURA_TELA, CHAO_Y, jogador1)
                jogador2.atacar(teclas_pressionadas, jogador1)

                if jogador1.hp <= 0: 
                    jogador1.hp = 0
                    estado_jogo = 'FIM_DE_JOGO'
                    mensagem_vitoria = "JOGADOR 2 VENCEU!"
                elif jogador2.hp <= 0: 
                    jogador2.hp = 0
                    estado_jogo = 'FIM_DE_JOGO'
                    mensagem_vitoria = "JOGADOR 1 VENCEU!"

            jogador1.desenhar(TELA)
            jogador2.desenhar(TELA)
            desenhar_barras_vida(jogador1.hp, jogador2.hp)

            if estado_jogo == 'FIM_DE_JOGO':
                fundo_escuro = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
                fundo_escuro.set_alpha(150) 
                fundo_escuro.fill(PRETO)
                TELA.blit(fundo_escuro, (0, 0))

                desenhar_texto_centralizado(mensagem_vitoria, FONTE_TITULO, VERDE_IFRN, -30)
                desenhar_texto_centralizado("Pressione ENTER para revanche", FONTE_SUBTITULO, BRANCO, 40)
                desenhar_texto_centralizado("Pressione ESC para o Menu", FONTE_SUBTITULO, BRANCO, 90)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()