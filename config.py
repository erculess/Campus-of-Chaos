import pygame

# Inicializa as fontes do PyGame
pygame.font.init()

# ==========================================
# CONFIGURAÇÕES DA TELA
# ==========================================
LARGURA_TELA = 1000
ALTURA_TELA = 600
FPS = 60
CHAO_Y = 550 # Altura onde a quadra começa

# ==========================================
# CORES (RGB)
# ==========================================
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE_IFRN = (46, 139, 87)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
CINZA = (100, 100, 100)

# ==========================================
# FONTES
# ==========================================
FONTE_TITULO = pygame.font.SysFont('arial', 64, bold=True)
FONTE_MENU = pygame.font.SysFont('arial', 40, bold=True)
FONTE_SUBTITULO = pygame.font.SysFont('arial', 32)
FONTE_CREDITOS = pygame.font.SysFont('arial', 28)

