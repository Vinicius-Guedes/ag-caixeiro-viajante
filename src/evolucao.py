import random
from src.geradorCidades import GeradorCidades
from src.populacao import Populacao
from src.reproducao import Reproducao


class Evolucao:
    def __init__(self, qtdeCidade, tamanhoPopulacao, limiteGeracoes) -> None:
        self.limiteGeracoes = limiteGeracoes
        self.qtdeCidade = qtdeCidade
        self.geracaoCidades = GeradorCidades( qtdeCidade )
        self.populacao = Populacao()
        self.populacao.valorTamanho(tamanhoPopulacao)
        self.taxa = 5

    def getGeracaoCidades(self) -> list:
        return self.geracaoCidades.cidades

    def definirParada(self) -> bool:
        return self.populacao.geracao >= self.limiteGeracoes

    def mutacao(self) -> None:
        for individuo in self.populacao.getIndividuos():
            sorteio = random.randint(0, 100)
            if sorteio < self.taxa:
                gene1 = random.randint(0, (self.qtdeCidade - 1))
                gene2 = random.randint(0, (self.qtdeCidade - 1))
                while gene1 == gene2:
                    gene2 = random.randint(0, (self.qtdeCidade - 1))
                individuo.inverterGene(gene1, gene2)

    def evoluir(self, log = True) -> list:
        self.populacao.iniciarPopulacao(self.qtdeCidade)
        self.populacao.calcularFitness(self.geracaoCidades.distancias)

        while True:
            if log:
                self.populacao.exibirPopulacao()
            if self.definirParada():
                break

            reproducao = Reproducao()
            reproducao.reproduzir(self.populacao, self.qtdeCidade)

            self.mutacao()

            self.populacao.calcularFitness(self.geracaoCidades.distancias)
            self.populacao.ajustarPopulacao()
            self.populacao.valorGeracao()

        if log:
            self.populacao.exibirSolucaoEncontrada()

        return [
            self.populacao.geracao, 
            self.populacao.individuos[0].getCromossomo(),
            self.populacao.individuos[0].fitness
        ]
