import random


class Reproducao:
    def __init__(self) -> None:
        self.selecionados = list()
        
    def sortearIndividuos(self, populacao):
        individuos = populacao.individuos.copy()

        for individuoPop in populacao.individuos:
            somaFitness = 0

            for individuo in individuos:
                somaFitness += individuo.fitness

            sorteio = random.randint(0, somaFitness) # -1
            posSorteada = -1

            while True:
                posSorteada += 1
                sorteio -= individuos[posSorteada].fitness
                if not sorteio > 0:
                    break

            self.selecionados.append(individuos[posSorteada])
            del individuos[posSorteada]

    def reproduzir(self, populacao, qtdeCidades):
        self.sortearIndividuos(populacao)

        for i in range(0, populacao.tamanho, 2):
            ponto1 = random.randint(0, (qtdeCidades - 2))
            ponto2 = None

            if ponto1 == 0:
                ponto2 = random.randint(0, ((qtdeCidades - 2) - (ponto1 + 1))) + (ponto1 + 1)
            else:
                ponto2 = random.randint(0, ((qtdeCidades - 1) - (ponto1 + 1))) + (ponto1 + 1) # Não subtrai por 1 no random

            filho1 = filho2 = [None] * qtdeCidades

            for j in range(ponto1, (ponto2 + 1)):
                filho1[j] = self.selecionados[i].cromossomo[j]
                filho2[j] = self.selecionados[i + 1].cromossomo[j]

            j = ponto2
            k = ponto2

            while True:
                j += 1

                if j == qtdeCidades:
                    j = 0
                if j == ponto1:
                    break 

                cidadeExiste = None
                while True:
                    k += 1

                    if k == qtdeCidades:
                        k = 0
                    if self.selecionados[i + 1].cromossomo[k] in filho1:
                        break
                filho1[j] = self.selecionados[i + 1].cromossomo[k]

            j = ponto2
            k = ponto2

            while True:
                j += 1

                if j == qtdeCidades:
                    j = 0
                if j == ponto1:
                    break 

                cidadeExiste = None
                while True:
                    k += 1

                    if k == qtdeCidades:
                        k = 0
                    if self.selecionados[i + 1].cromossomo[k] in filho2:
                        break
                filho2[j] = self.selecionados[i + 1].cromossomo[k]

        populacao.addFilhos(filho1, filho2)
