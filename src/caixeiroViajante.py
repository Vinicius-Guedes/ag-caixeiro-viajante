from evolucao import Evolucao


class CaixeiroViajante:
    def __init__(self, qtdeCidade, tamanhoPopulacao, limiteGeracoes) -> None:
        self.evolucao = Evolucao(qtdeCidade, tamanhoPopulacao, limiteGeracoes)
    
    def getGeracaoCidades(self) -> list:
        return self.evolucao.getGeracaoCidades()

    def run(self, log = True) -> None:
        return self.evolucao.evoluir(log)

if __name__ == '__main__':
    caixeiroViajante = CaixeiroViajante(10, 6, 100)
    caixeiroViajante.run()
