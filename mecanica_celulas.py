class obj:
    def __init__(self, rect, cond, bomb, rast):
        self.rect = rect # Coordenadas do rec para printar
        self.cond = cond # 0 - Não Revelada; 1 - Revelada; 2 - Marcada
        self.bomb = bomb # 0 - Não tem bomba; 1 - Tem bomba
        self.rast = rast # Número detectado de minas em volta







