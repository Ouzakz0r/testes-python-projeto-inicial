from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):
    def setUp(self):
        self.gabriel = Usuario("Gabriel", 500.0)
        self.gustavo = Usuario("Gustavo", 500.0)

        self.lance_gabriel = Lance(self.gabriel, 200.0)
        self.lance_gustavo = Lance(self.gustavo, 100.0)

        self.leilao = Leilao("leilao de celular")

    def test_quando_lances_em_ordem_crescente_deve_retornar_maior_e_menor_lance(self):
        self.leilao.dar_lance(self.lance_gustavo)
        self.leilao.dar_lance(self.lance_gabriel)

        maior_valor_esperado = 200.0
        menor_valor_esperado = 100.0

        self.assertEqual(self.leilao.menor_lance, menor_valor_esperado)
        self.assertEqual(self.leilao.maior_lance, maior_valor_esperado)

    def test_quando_lances_em_ordem_decrescente_nao_deve_permitir_lance(self):
        with self.assertRaises(LanceInvalido):

            self.leilao.dar_lance(self.lance_gabriel)
            self.leilao.dar_lance(self.lance_gustavo)

    def test_quando_houver_apenas_um_lance_deve_retornar_o_mesmo_valor_para_maior_e_menor_lances(self):
        self.leilao.dar_lance(self.lance_gabriel)

        maior_valor_esperado = 200.0
        menor_valor_esperado = 200.0

        self.assertEqual(self.leilao.menor_lance, menor_valor_esperado)
        self.assertEqual(self.leilao.maior_lance, maior_valor_esperado)

    def test_quando_houver_mais_de_dois_lances_deve_retornar_maior_e_menor_lance(self):
        karol = Usuario("Karoline", 500.0)
        lance_karol = Lance(karol, 150.0)

        self.leilao.dar_lance(self.lance_gustavo)
        self.leilao.dar_lance(lance_karol)
        self.leilao.dar_lance(self.lance_gabriel)


        maior_valor_esperado = 200.0
        menor_valor_esperado = 100.0

        self.assertEqual(self.leilao.menor_lance, menor_valor_esperado)
        self.assertEqual(self.leilao.maior_lance, maior_valor_esperado)

    def test_quando_nao_houver_lances_deve_permitir_dar_lance(self):
        self.leilao.dar_lance(self.lance_gabriel)

        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances)

    def test_quando_usuarios_diferentes_propoem_lance_em_sequencia_deve_permitir_dar_lance(self):
        self.leilao.dar_lance(self.lance_gustavo)
        self.leilao.dar_lance(self.lance_gabriel)

        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances)

    def test_quando_o_mesmo_usuario_propoe_lances_seguidos_deve_barrar_o_lance(self):
        segundo_lance_do_gabriel = Lance(self.gabriel, 300)

        with self.assertRaises(LanceInvalido):
            self.leilao.dar_lance(self.lance_gabriel)
            self.leilao.dar_lance(segundo_lance_do_gabriel)


