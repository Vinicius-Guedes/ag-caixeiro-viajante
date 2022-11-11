import random


class Reproducao:
    def __init__(self) -> None:
        self.selecionados = list()

    def melhoresIndividuos(self, populacao):
        individuos = populacao.getIndividuos()

        return (individuos[0].getCromossomo(), individuos[1].getCromossomo())

    def reproduzir(self, populacao, qtdeCidades):
        pai1, pai2 = self.melhoresIndividuos(populacao)

        # Cruzamento Order Crossover (OX)
        ponto1 = random.randint(0, (qtdeCidades - 3))
        ponto2 = random.randint((ponto1 + 1), (qtdeCidades - 2))

        filho1 = [None] * qtdeCidades
        filho2 = [None] * qtdeCidades

        for j in range(ponto1, (ponto2 + 1)):
            filho1[j] = pai1[j]
            filho2[j] = pai1[::-1][j]

        for i in pai2:
            if not i in filho1:
                filho1[filho1.index(None)] = i

        for i in pai2[::-1]:
            if not i in filho2:
                filho2[filho2.index(None)] = i

        populacao.addFilhos(filho1, filho2)
