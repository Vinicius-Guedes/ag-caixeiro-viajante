import random

class Cidade:
    def __init__(self) -> None:
        self.pontoX = 0
        self.pontoY = 0
        self.id = 0
        self.conexoes = list()
    
    def setCoordenada(self) -> None:
        self.pontoX = random.randint(1,100)
        self.pontoY = random.randint(1,100)
