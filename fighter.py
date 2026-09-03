import pygame
from config import *

class Lutador:
    def __init__(self, x, y, cor, controles):
        self.rect = pygame.Rect(x, y, 60, 120)
        self.cor = cor
        self.controles = controles

        self.hp_max = 100
        self.hp = self.hp_max
        self.velocidade = 6
        
        self.vel_x = 0
        self.vel_y = 0
        self.pulo_forca = -15
        self.gravidade = 0.8
        self.no_chao = False
        self.agachado = False

        self.hitstun = 0
        self.atacando = False
        self.defendendo = False
        self.tempo_ataque = 0
        self.hitbox = pygame.Rect(0, 0, 0, 0)
        self.olhando_direita = True if x < LARGURA_TELA/2 else False

    def receber_golpe(self, dano, empurrao_x, duracao_stun):
        self.hp -= dano
        self.vel_x = empurrao_x
        self.hitstun = duracao_stun
        
        self.atacando = False
        self.hitbox = pygame.Rect(0, 0, 0, 0)

    def mover(self, largura_tela, altura_chao, oponente):
        dx = 0
        dy = 0
        
        self.agachado = False
        self.defendendo = False

        if self.hitstun > 0:
            self.hitstun -= 1
            dx = self.vel_x  # O jogador não controla o personagem; ele desliza pelo knockback
        else:
            # Entrada normal de comandos quando NÃO está em hitstun
            teclas = pygame.key.get_pressed()

            if teclas[self.controles['defesa']] and self.no_chao:
                self.defendendo = True
            
            if not self.atacando and not self.defendendo:
                if teclas[self.controles['agachar']]:
                    self.agachado = True
                    self.rect.height = 80
                    dy += 40 
                else:
                    self.rect.height = 120
                    if teclas[self.controles['esquerda']]:
                        dx = -self.velocidade
                        self.olhando_direita = False
                    if teclas[self.controles['direita']]:
                        dx = self.velocidade
                        self.olhando_direita = True

                if teclas[self.controles['pulo']] and self.no_chao:
                    self.vel_y = self.pulo_forca
                    self.no_chao = False

        self.vel_x *= 0.85
        if abs(self.vel_x) < 0.5:
            self.vel_x = 0

        self.vel_y += self.gravidade
        dy += self.vel_y

        if self.rect.bottom + dy >= altura_chao:
            self.vel_y = 0
            dy = altura_chao - self.rect.bottom
            self.no_chao = True

        rect_teste_x = self.rect.copy()
        rect_teste_x.x += dx
        
        if rect_teste_x.colliderect(oponente.rect):
            if self.rect.bottom > oponente.rect.top:
                if dx > 0: 
                    dx = oponente.rect.left - self.rect.right
                elif dx < 0: 
                    dx = oponente.rect.right - self.rect.left

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > largura_tela:
            dx = largura_tela - self.rect.right
            self.vel_x = 0

        self.rect.x += dx
        self.rect.y += dy

    def atacar(self, teclas, alvo):
        if not self.atacando and not self.defendendo and self.hitstun == 0:
            if teclas[self.controles['soco_fraco']] or teclas[self.controles['soco_forte']]:
                self.atacando = True
                self.tempo_ataque = 20 
                
                hitbox_largura = 50
                hitbox_altura = 20
                
                if self.olhando_direita:
                    self.hitbox = pygame.Rect(self.rect.centerx, self.rect.y + 20, hitbox_largura, hitbox_altura)
                    direcao = 1
                else:
                    self.hitbox = pygame.Rect(self.rect.centerx - hitbox_largura, self.rect.y + 20, hitbox_largura, hitbox_altura)
                    direcao = -1
                
                if self.hitbox.colliderect(alvo.rect):
                    if alvo.defendendo:
                        alvo.receber_golpe(dano=2, empurrao_x=direcao * 4, duracao_stun=5)
                    else:
                        alvo.receber_golpe(dano=10, empurrao_x=direcao * 12, duracao_stun=18)

        if self.atacando:
            self.tempo_ataque -= 1
            if self.tempo_ataque <= 0:
                self.atacando = False
                self.hitbox = pygame.Rect(0, 0, 0, 0) 

    def desenhar(self, superficie):
        if self.hitstun > 0:
            cor_atual = VERMELHO if (self.hitstun // 3) % 2 == 0 else BRANCO
        elif self.defendendo:
            cor_atual = AMARELO
        else:
            cor_atual = self.cor

        pygame.draw.rect(superficie, cor_atual, self.rect)
        if self.atacando:
            pygame.draw.rect(superficie, VERMELHO, self.hitbox)

