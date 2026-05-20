class Personagem:
    """Classe Pai para todos os personagns jogaveis"""
    def __init__(self, nome, vida_maxima):
        self.nome = nome
        self.vida = vida_maxima
        self.vivo = True

    def mover(self, direcao):
        print(f" [{self.nome}] moveu-se para {direcao}.")

    def receber_dano(self, quantidade):
        self.vida -= quantidade
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False
            print(f" [{self.nome}] caiu em combate e precisa de ajuda!")
        else:
            print(f" [{self.nome}] sofreu {quantidade} de dano! (Vida restante: {self.vida})")

#CLASSES FILHAS = personagens

class Hopper(Personagem):
    def __init__(self):
        super().__init__(nome="Jim Hopper", vida_maxima=150)
        
    def atacar_soco(self, inimigo):
        if self.vivo and inimigo.vivo:
            print(f" [{self.nome}] desfere um soco pesado em {inimigo.nome}!")
            inimigo.receber_dano(25)

class Lucas(Personagem):
    def __init__(self):
        super().__init__(nome="Lucas Sinclair", vida_maxima=100)
        
    def ataque_estilingue(self, inimigo):
        if self.vivo and inimigo.vivo:
            print(f" [{self.nome}] dispara um explosivo com o estilingue em {inimigo.nome}!")
            inimigo.receber_dano(20)

class Max(Personagem):
    def __init__(self):
        super().__init__(nome="Max Mayfield", vida_maxima=90)
        
    def chutar(self, inimigo):
        if self.vivo and inimigo.vivo:
            print(f" [{self.nome}] acerta um chute ágil e direto em {inimigo.nome}!")
            inimigo.receber_dano(15)
        
    def curar_aliado(self, aliado):
        if self.vivo and aliado.vida > 0:
            cura = 30
            aliado.vida += cura
            print(f" [{self.nome}] ajudou {aliado.nome}, curando {cura} de vida! (Vida atual: {aliado.vida})")

class Nancy(Personagem):
    def __init__(self):
        super().__init__(nome="Nancy Wheeler", vida_maxima=110)
        
    def ataque_tesoura(self, inimigo):
        if self.vivo and inimigo.vivo:
            print(f" [{self.nome}] avança com a tesoura, aplicando uma estocada precisa em {inimigo.nome}!")
            inimigo.receber_dano(22)

class Mike(Personagem):
    def __init__(self):
        super().__init__(nome="Mike Wheeler", vida_maxima=100)
        
    def ataque_bastao(self, inimigo):
        if self.vivo and inimigo.vivo:
            print(f" [{self.nome}] balança seu taco de beisebol, atingindo {inimigo.nome} em cheio!")
            inimigo.receber_dano(20)

class Will(Personagem):
    def __init__(self):
        super().__init__(nome="Will Byers", vida_maxima=90)
        
    def disparar_fogos(self, grupo_inimigos):
        if self.vivo:
            print(f" [{self.nome}] dispara fogos de artifício em área!")
            for inimigo in grupo_inimigos:
                if inimigo.vivo:
                    inimigo.receber_dano(15)

class Dustin(Personagem):
    def __init__(self):
        super().__init__(nome="Dustin Henderson", vida_maxima=100)
        
    def spray_quimico(self, inimigo):
        if self.vivo and inimigo.vivo:
            print(f" [{self.nome}] usa o spray químico em {inimigo.nome}, causando dano contínuo!")
            inimigo.receber_dano(18)
        
    def hackear(self, terminal):
        if self.vivo:
            print(f" [{self.nome}] conectou-se ao {terminal} e está quebrando a segurança da rede...")

class Onze(Personagem):
    def __init__(self):
        super().__init__(nome="Onze (Eleven)", vida_maxima=80)
        
    def ataque_mental(self, inimigo):
        if self.vivo and inimigo.vivo:
            print(f" [{self.nome}] canaliza seus poderes telecinéticos contra {inimigo.nome}!")
            inimigo.receber_dano(45)

class Joyce(Personagem):
    def __init__(self):
        super().__init__(nome="Joyce Byers", vida_maxima=110)
        
    def usar_cortador_parafusos(self, obstaculo):
        if self.vivo:
            print(f" [{self.nome}] usa o cortador de parafusos para romper {obstaculo} e abrir caminho.")

class Jhonatan(Personagem):
    def __init__(self):
        super().__init__(nome="Jhonatan Byers", vida_maxima=100)
        
    def flash_camera(self, grupo_inimigos):
        if self.vivo:
            print(f" [{self.nome}] dispara o flash da câmera! Todos os inimigos visíveis estão atordoados!")
            # O atordoamento poderia pular o turno do inimigo na lógica principal do jogo

class Eddie(Personagem):
    def __init__(self):
        super().__init__(nome="Eddie Munson", vida_maxima=120)
        
    def solo_guitarra(self):
        if self.vivo:
            print(f" [{self.nome}] começa um solo insano! Ondas sonoras atraem e atordoam os Demobats!")

class Robin(Personagem):
    def __init__(self):
        super().__init__(nome="Robin Buckley", vida_maxima=100)
        
    def identificar_enigma(self, pista):
        if self.vivo:
            print(f" [{self.nome}] analisa a pista '{pista}' e soluciona o enigma!")