import random
from cidade import Cidade
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
            qtdeConexoes = random.randint(2, 4)

            for id in self.cidades:
                if cidade.id in id.conexoes:
                    cidade.conexoes.append(id.id)
            if len(cidade.conexoes) >= qtdeConexoes:
                continue
        
            qtdeConexoes = qtdeConexoes - len(cidade.conexoes)

            if cidade.id == (self.qtdeCidade - 1):
                continue

            for c in range(0, qtdeConexoes):
                while True:
                    conexao = random.randint(0, (self.qtdeCidade - 1))
                    if not conexao in cidade.conexoes and not conexao == cidade.id and cidade.id < conexao:
                        cidade.conexoes.append(conexao)
                        break

    def definirDistancias(self) -> None:
        for cidade in self.cidades:
            distancia = list()
            for cidade2 in self.cidades:
                if cidade2.id in cidade.conexoes or cidade2.id == cidade.id:
                    aux1 = (cidade.pontoX - cidade2.pontoX) ** 2
                    aux2 = (cidade.pontoY - cidade2.pontoY) ** 2
                    distancia.append( int(math.sqrt(aux1 + aux2)) )
                else:
                    distancia.append(0)
            self.distancias.append(distancia)

if __name__ == "__main__":
    teste = GeradorCidades(10)
    for linha in teste.distancias:
        print(linha)
