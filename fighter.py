import pygame
from config import *

class Lutador:
    def __init__(self, x, y, cor, controles):
        self.rect = pygame.Rect(x, y, 60, 120)
        self.cor = cor
        self.controles = controles
        
        self.hp = 100
        self.velocidade = 6
        
        self.vel_y = 0
        self.pulo_forca = -15
        self.gravidade = 0.8
        self.no_chao = False
        self.agachado = False
        
        self.atacando = False
        self.defendendo = False
        self.tempo_ataque = 0
        self.hitbox = pygame.Rect(0, 0, 0, 0)
        self.olhando_direita = True if x < LARGURA_TELA/2 else False

    def mover(self, largura_tela, altura_chao, oponente):
        teclas = pygame.key.get_pressed()
        dx = 0
        dy = 0
        
        self.agachado = False
        self.defendendo = False

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

        self.rect.x += dx
        self.rect.y += dy

    def atacar(self, teclas, alvo):
        if not self.atacando and not self.defendendo:
            if teclas[self.controles['soco_fraco']] or teclas[self.controles['soco_forte']]:
                self.atacando = True
                self.tempo_ataque = 20 
                
                hitbox_largura = 50
                hitbox_altura = 20
                
                if self.olhando_direita:
                    self.hitbox = pygame.Rect(self.rect.centerx, self.rect.y + 20, hitbox_largura, hitbox_altura)
                else:
                    self.hitbox = pygame.Rect(self.rect.centerx - hitbox_largura, self.rect.y + 20, hitbox_largura, hitbox_altura)
                
                if self.hitbox.colliderect(alvo.rect):
                    if alvo.defendendo:
                        alvo.hp -= 2 
                    else:
                        alvo.hp -= 10 

        if self.atacando:
            self.tempo_ataque -= 1
            if self.tempo_ataque <= 0:
                self.atacando = False
                self.hitbox = pygame.Rect(0, 0, 0, 0) 

    def desenhar(self, superficie):
        cor_atual = AMARELO if self.defendendo else self.cor
        pygame.draw.rect(superficie, cor_atual, self.rect)
        if self.atacando:
            pygame.draw.rect(superficie, VERMELHO, self.hitbox)

