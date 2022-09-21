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

    def valorGeracao(self):
        self.geracao += 1
    
    def iniciarPopulacao(self, qtdeCidades):
        for c in range(0, self.tamanho):
            individuo = Individuo()

            individuo.cromossomoInicial(qtdeCidades)
            self.individuos.append(individuo)
    
    def calcularFitness(self, distancias):
        def myKey(a):
            return a[0] - a[1]

        for individuo in self.individuos:
            fitness = 0
            lastIndex = False

            for index, cromossomo in enumerate(individuo.cromossomo):
                cidadeA = cromossomo
                cidadeB = individuo.cromossomo[index + 1]

                fitness += distancias[cidadeA, cidadeB]
                lastIndex = index

            cidadeA = individuo.cromossomo[lastIndex]
            cidadeB = individuo.cromossomo[0]
            fitness += distancias[cidadeA, cidadeB]

            individuo.fitness = fitness

        self.individuos.sort(key=myKey)

    def addFilhos(self, filho1, filho2):
        individuo = Individuo()
        individuo.cromossomo = filho1
        self.individuos.append(individuo)

        individuo = Individuo()
        individuo.cromossomo = filho2
        self.individuos.append(individuo)

    def ajustarPopulacao(self):
        self.individuos[:self.tamanho]

    def exibirPopulacao(self):
        cromossomo = list()
        fitness = list()

        for index, individuo in enumerate(self.individuos):
            cromossomo[index] = individuo.cromossomo
            fitness[index] = individuo.fitness
        
        print("Populacao: ")
        print(cromossomo)
        print("Fitness: ")
        print(fitness)
        print("Geracao: " + self.geracao)
        print("-=-" * 20)

    def exibirSolucaoEncontrada(self):
        print("Solução encontrada:")
        print("Individuo: " + self.individuos[0].cromossomo)
        print("Menor distancia: " + self.individuos[0].fitness)
