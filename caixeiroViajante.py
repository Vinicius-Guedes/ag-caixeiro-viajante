from src.evolucao import Evolucao


class CaixeiroViajante:
    def __init__(self, qtdeCidade, tamanhoPopulacao, limiteGeracoes, cidadeInicial) -> None:
        self.evolucao = Evolucao(qtdeCidade, tamanhoPopulacao, limiteGeracoes, cidadeInicial)
    
    def getGeracaoCidades(self) -> list:
        return self.evolucao.getGeracaoCidades()

    def run(self, log = True) -> list:
        return self.evolucao.evoluir(log)

if __name__ == '__main__':
    caixeiroViajante = CaixeiroViajante(10, 6, 100, 3)
    caixeiroViajante.run()
