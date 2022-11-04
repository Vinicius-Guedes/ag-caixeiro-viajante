import random
from geradorCidades import GeradorCidades
from populacao import Populacao
from reproducao import Reproducao


class Evolucao:
    def __init__(self, qtdeCidade, tamanhoPopulacao, limiteGeracoes = 'infinita') -> None:
        self.limiteGeracoes = limiteGeracoes
        self.qtdeCidade = qtdeCidade
        self.geracaoCidades = GeradorCidades( qtdeCidade )
        self.populacao = Populacao()
        self.populacao.valorTamanho(tamanhoPopulacao)
        self.taxa = 5
    
    def definirParada(self) -> bool:
        if self.limiteGeracoes == 'infinita':
            return False
        
        return self.populacao.geracao >= self.limiteGeracoes
    
    def mutacao(self):
        for individuo in self.populacao.individuos:
            sorteio = random.randint(0, 100)
            if sorteio < self.taxa:
                gene1 = random.randint(0, (self.qtdeCidade - 1))
                gene2 = random.randint(0, (self.qtdeCidade - 1))
                while gene1 == gene2:
                    gene2 = random.randint(0, (self.qtdeCidade - 1))
                individuo.inverterGene(gene1, gene2)
    
    def evoluir(self):
        self.populacao.iniciarPopulacao(self.qtdeCidade)
        self.populacao.calcularFitness(self.geracaoCidades.distancias)

        while True:
            self.populacao.exibirPopulacao()
            if self.definirParada():
                break

            reproducao = Reproducao()
            reproducao.reproduzir(self.populacao, self.qtdeCidade)

            self.mutacao()

            self.populacao.calcularFitness(self.geracaoCidades.distancias)
            self.populacao.ajustarPopulacao()
            self.populacao.valorGeracao()

        self.populacao.exibirSolucaoEncontrada()
