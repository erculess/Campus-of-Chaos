import pygame
from config import *
from fighter import Lutador

class Rickson(Lutador):
    def __init__(self, x, y, controles):
        # Baseado em Jax: Roupas escuras, tanque, lento
        super().__init__(x, y, PRETO, controles)
        
        # Atributos específicos
        self.hp_max = 120  # Mais vida
        self.hp = self.hp_max
        self.velocidade = 4  # Movimentação mais pesada
        self.pulo_forca = -13 # Pula mais baixo

    # Exemplo de como sobrescreveremos um ataque no futuro
    # def atacar(self, teclas, alvo):
    #     Lógica de um soco mais forte e lento aqui...


class Mirelly(Lutador):
    def __init__(self, x, y, controles):
        # Baseada em Kitana: Roupa azul, ágil
        super().__init__(x, y, AZUL, controles)
        
        # Atributos específicos
        self.hp_max = 90   # Menos vida (mais frágil)
        self.hp = self.hp_max
        self.velocidade = 8  # Movimentação bem mais rápida
        self.pulo_forca = -17 # Pula mais alto