import pygame


pygame.init()
TELA_LARGURA = 1024
TELA_ALTURA = 678
MAX_FPS = 30

class Interface:
    def __init__(self, distancias, cidades) -> None:
        self.tela = pygame.display.set_mode(( TELA_LARGURA, TELA_ALTURA ))
        pygame.display.set_caption('Caixeiro Viajante')
        self.clock = pygame.time.Clock()
        self.tela.fill(pygame.Color(40, 40, 40))
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.rodando = True

        self.distancias = distancias
        self.cidades = cidades
    
    def desenhaCaminhos(self) -> None:
        for index, cidade in enumerate(self.distancias):
            for index2, distancia in enumerate(cidade):
                if not distancia == 0:
                    pygame.draw.line(self.tela, (40, 40, 255), 
                        (int(4.5 * self.cidades[index].pontoX), int(4.5 * self.cidades[index].pontoY)), 
                        (int(4.5 * self.cidades[index2].pontoX), int(4.5 * self.cidades[index2].pontoY))
                    )

    def desenhaCidades(self) -> None:
        for cidade in self.cidades:
            pygame.draw.circle(self.tela, (255, 40, 40), (int(4.5 * cidade.pontoX), int(4.5 * cidade.pontoY)), 4)
            text_surface = self.font.render(str(cidade.id), False, (40, 255, 40))
            self.tela.blit(text_surface, (int(4.5 * cidade.pontoX), int(4.5 * cidade.pontoY)))

    def desenhaMapa(self) -> None:
        self.desenhaCaminhos()
        self.desenhaCidades()


    def run(self) -> None:
        while self.rodando:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.rodando = False

            self.tela.fill(pygame.Color(40, 40, 40))

            self.desenhaMapa()

            self.clock.tick(MAX_FPS)
            pygame.display.update()
