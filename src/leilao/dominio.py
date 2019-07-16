from src.leilao.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__carteira = saldo

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propor_lance(self, leilao, valor):
        if self._valor_valido(valor):
            lance = Lance(self, valor)
            leilao.dar_lance(lance)
            self.__carteira -= valor

    def _valor_valido(self, valor):
        if self.__carteira >= valor:
            return True
        raise LanceInvalido("Saldo indisponível em carteira para executar o lance")


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    def dar_lance(self, lance):
        if self._lance_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor
            self.__lances.append(lance)

    def _lance_valido(self, lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance) and
                                          self._valor_maior_que_o_lance_anterior(lance))

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuário não pode dar dois lances seguidos")

    def _valor_maior_que_o_lance_anterior(self, lance):
        if self.__lances[-1].valor < lance.valor:
            return True
        raise LanceInvalido("O valor do lance deve ser maior que o lance anterior")

