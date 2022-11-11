import random


class Individuo:
    def __init__(self) -> None:
        self.cromossomo = list()
        self.fitness = 0

    def getCromossomo(self):
        return self.cromossomo.copy()

    def cromossomoInicial(self, qtdeCidades) -> None:
        while len(self.cromossomo) < qtdeCidades:
            cidadeAleatoria = random.randint(0, (qtdeCidades - 1))

            if not cidadeAleatoria in self.cromossomo:
                self.cromossomo.append(cidadeAleatoria)

    def inverterGene(self, gene1, gene2) -> None:
        self.cromossomo[gene1], self.cromossomo[gene2] = self.cromossomo[gene2], self.cromossomo[gene1]
