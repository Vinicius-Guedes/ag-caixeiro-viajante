from src.cidade import Cidade
import math


class GeradorCidades:
    def __init__(self, qtdeCidade) -> None:
        self.qtdeCidade = qtdeCidade
        self.cidades = list()
        self.distancias = list()
        self.criarCidades()
        self.definirDistancias()

    def criarCidades(self) -> None:
        for id in range(0, self.qtdeCidade):
            cidade = Cidade()
            cidade.setCoordenada()
            cidade.id = id
            self.cidades.append(cidade)

    def definirDistancias(self) -> None:
        for cidade in self.cidades:
            distancia = list()
            for cidade2 in self.cidades:
                aux1 = (cidade.pontoX - cidade2.pontoX) ** 2
                aux2 = (cidade.pontoY - cidade2.pontoY) ** 2
                distancia.append( int(math.sqrt(aux1 + aux2)) )
            self.distancias.append(distancia)


if __name__ == "__main__":
    teste = GeradorCidades(10)
    for linha in teste.distancias:
        print(linha)
