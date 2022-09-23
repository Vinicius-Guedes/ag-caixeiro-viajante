import random


class Reproducao:
    def __init__(self) -> None:
        self.selecionados = list()
         
    def sortearIndividuos(self, populacao):
        individuos = populacao.individuos

        for individuoPop in populacao.individuos:
            somaFitness = 0

            for individuo in individuos:
                somaFitness += individuo.fitness
            
            sorteio = random.randint(0, (somaFitness - 1))
            posSorteada = -1

            while True:
                posSorteada += 1
                sorteio -= individuos[posSorteada].fitness
                if sorteio > 0:
                    break
            
            self.selecionados.append(individuos[posSorteada])
            del individuos[posSorteada]

    def reproduzir(self, populacao, qtdeCidades):
        self.sortearIndividuos(populacao)

        for c in range(0, populacao.tamanho, 2):
            ponto1 = random.randint(0, (qtdeCidades - 2))#pode ser menos 1

            if ponto1 == 0:
                ponto2 = random.randint(0, ((qtdeCidades - 3) - (ponto1 + 1))) + (ponto1 + 1)
            else:
                ponto2 = random.randint(0, ((qtdeCidades - 2) - (ponto1 + 1))) + (ponto1 + 1)
            
            filho1, filho2 = list()
            for i in range(ponto1, (ponto2 + 1)):
                filho1[i] = self.selecionados[c].cromossomo[c]
                filho2[i] = self.selecionados[c + 1].cromossomo[c]
            
            j, k = ponto2

            while True:
                j += 1
                if j == qtdeCidades:
                    j = 0
                if j == ponto1:
                    break

                while True:
                    k += 1
                    if k == qtdeCidades:
                        k = 0
                    if not filho1 in self.selecionados[c + 1].cromossomo[k]:
                        break

                filho1[j] = self.selecionados[i + 1].cromossomo[k]
                
            j, k = ponto2
            while True:
                j += 1
                if j == qtdeCidades:
                    j = 0
                if j == ponto1:
                    break

                while True:
                    k += 1
                    if k == qtdeCidades:
                        k = 0
                    if not filho2 in self.selecionados[i].cromossomo[k]:
                        break

                filho2[j] = self.selecionados[i].cromossomo[k]
        
            populacao.addFilhos(filho1, filho2)
