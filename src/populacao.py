from individuo import Individuo


class Populacao:
    def __init__(self) -> None:
       self.tamanho = 0
       self.individuos = list()
       self.geracao = 1

    def valorTamanho(self, tamanho) -> None:
        if tamanho <= 0:
            print("ERRO: Tamanho nao pode ser 0!")
            return
        
        self.tamanho =  tamanho if tamanho % 2 == 0 else tamanho + 1

    def valorGeracao(self) -> None:
        self.geracao += 1

    def iniciarPopulacao(self, qtdeCidades) -> None:
        for c in range(0, self.tamanho):
            individuo = Individuo()

            individuo.cromossomoInicial(qtdeCidades)
            self.individuos.append(individuo)
    
    def calcularFitness(self, distancias) -> None:
        def myKey(a):
            return a.fitness

        for individuo in self.individuos:
            fitness = 0

            for index, cromossomo in enumerate(individuo.cromossomo):
                if len(individuo.cromossomo) == (index + 1):
                    break

                cidadeA = cromossomo
                cidadeB = individuo.cromossomo[index + 1]

                fitness += distancias[cidadeA][cidadeB]

            cidadeA = individuo.cromossomo[len(individuo.cromossomo) - 1]
            cidadeB = individuo.cromossomo[0]
            fitness += distancias[cidadeA][cidadeB]

            individuo.fitness = fitness

        self.individuos.sort(key=myKey)

    def addFilhos(self, filho1, filho2) -> None:
        individuo = Individuo()
        individuo.cromossomo = filho1
        self.individuos.append(individuo)

        individuo = Individuo()
        individuo.cromossomo = filho2
        self.individuos.append(individuo)

    def ajustarPopulacao(self) -> None:
        self.individuos[:self.tamanho]

    def exibirPopulacao(self) -> None:
        cromossomo = list()
        fitness = list()

        for index, individuo in enumerate(self.individuos):
            cromossomo.append(individuo.cromossomo)
            fitness.append(individuo.fitness)
        
        print("Populacao: ")
        print(cromossomo)
        print("Fitness: ")
        print(fitness)
        print("Geracao: " + str(self.geracao))
        print("-=-" * 20)

    def exibirSolucaoEncontrada(self) -> None:
        print("Solução encontrada:")
        print("Individuo: ", self.individuos[0].cromossomo)
        print("Menor distancia: ", self.individuos[0].fitness)
