class Inimigo:
    """Classe Pai para todos os inimigos"""
    def __init__(self, nome, vida, dano_base):
        self.nome = nome
        self.vida = vida
        self.dano_base = dano_base
        self.vivo = True

    def mover(self):
        print(f"[{self.nome}] está se aproximando ameaçadoramente...")

    def receber_dano(self, quantidade):
        self.vida -= quantidade
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False
            print(f" O inimigo {self.nome} foi derrotado!")
        else:
            print(f" [{self.nome}] recebeu {quantidade} de dano! (Vida: {self.vida})")

    def atacar(self, alvo):
        if self.vivo and alvo.vivo:
            print(f"[{self.nome}] ataca {alvo.nome}!")
            alvo.receber_dano(self.dano_base)

#CLASSES FILHA = inimigos

class Guarda(Inimigo):
    def __init__(self, tipo_ataque="bater"):
        dano = 10 if tipo_ataque == "bater" else 20
        super().__init__(nome=f"Guarda Russo ({tipo_ataque})", vida=50, dano_base=dano)
        self.tipo_ataque = tipo_ataque

    def atacar(self, alvo):
        if self.vivo and alvo.vivo:
            if self.tipo_ataque == "bater":
                print(f" [{self.nome}] avança e tenta bater em {alvo.nome} com um cassetete!")
            else:
                print(f" [{self.nome}] mira sua AK-47 e atira em {alvo.nome}!")
            alvo.receber_dano(self.dano_base)

class Demogorgon(Inimigo):
    def __init__(self):
        super().__init__(nome="Demogorgon", vida=150, dano_base=30)

    def atacar(self, alvo):
        if self.vivo and alvo.vivo:
            print(f" [{self.nome}] ruge e rasga {alvo.nome} com suas garras!")
            alvo.receber_dano(self.dano_base)

class Demodog(Inimigo):
    def __init__(self):
        super().__init__(nome="Demodog", vida=80, dano_base=25)

    def atacar(self, alvo):
        if self.vivo and alvo.vivo:
            print(f"[{self.nome}] corre sobre 4 patas e salta para morder {alvo.nome}!")
            alvo.receber_dano(self.dano_base)

class MindFlayer(Inimigo):
    def __init__(self):
        super().__init__(nome="Mind Flayer", vida=500, dano_base=50)

    def atacar(self, alvo):
        if self.vivo and alvo.vivo:
            print(f" [{self.nome}] ataca {alvo.nome} com seus tentáculos sombrios!")
            alvo.receber_dano(self.dano_base)

class Demobat(Inimigo):
    def __init__(self):
        super().__init__(nome="Demobat (Demoert)", vida=30, dano_base=10)

    def atacar(self, alvo):
        if self.vivo and alvo.vivo:
            print(f" [{self.nome}] faz um mergulho rasante para morder {alvo.nome}!")
            alvo.receber_dano(self.dano_base)

class Vecna(Inimigo):
    def __init__(self):
        super().__init__(nome="Vecna", vida=300, dano_base=45)

    def atacar(self, alvo):
        if self.vivo and alvo.vivo:
            print(f" [{self.nome}] invade a mente de {alvo.nome} com poderes telecinéticos e visões macabras!")
            alvo.receber_dano(self.dano_base)



