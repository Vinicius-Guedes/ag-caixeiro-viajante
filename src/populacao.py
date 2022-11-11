from individuo import Individuo


class Populacao:
    def __init__(self) -> None:
       self.tamanho = 0
       self.individuos = list()
       self.geracao = 1

    def getIndividuos(self):
        return self.individuos.copy()

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
        for individuo in self.individuos:
            fitness = 0
            for index, cromossomo in enumerate(individuo.getCromossomo()):
                if len(individuo.getCromossomo()) == (index + 1):
                    break

                cidadeA = individuo.getCromossomo()[index]
                cidadeB = individuo.getCromossomo()[index + 1]

                fitness += distancias[cidadeA][cidadeB]

            cidadeA = individuo.getCromossomo()[len(individuo.getCromossomo()) - 1]
            cidadeB = individuo.getCromossomo()[0]
            fitness += distancias[cidadeA][cidadeB]

            individuo.fitness = fitness

        self.individuos.sort(key=lambda a: a.fitness)

    def addFilhos(self, filho1, filho2) -> None:
        individuo = Individuo()
        individuo.cromossomo = filho1
        self.individuos.append(individuo)

        individuo = Individuo()
        individuo.cromossomo = filho2
        self.individuos.append(individuo)

    def ajustarPopulacao(self) -> None:
        self.individuos = self.individuos[:self.tamanho]

    def exibirPopulacao(self) -> None:
        cromossomo = list()
        fitness = list()

        for index, individuo in enumerate(self.individuos):
            cromossomo.append(individuo.getCromossomo())
            fitness.append(individuo.fitness)
        
        print("Populacao: ")
        print(cromossomo)
        print("Fitness: ")
        print(fitness)
        print("Geracao: " + str(self.geracao))
        print("-=-" * 20)

    def exibirSolucaoEncontrada(self) -> None:
        print("Solução encontrada:")
        print("Individuo: ", self.individuos[0].getCromossomo())
        print("Menor distancia: ", self.individuos[0].fitness)
