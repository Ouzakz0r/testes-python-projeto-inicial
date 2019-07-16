import pytest

from src.leilao.dominio import Usuario, Leilao
from src.leilao.excecoes import LanceInvalido


@pytest.fixture
def gabriel():
    return Usuario("Gabriel", 100.0)


@pytest.fixture
def leilao():
    return Leilao("Leilão de notebook")


def test_quando_propor_um_lance_deve_subtrair_do_saldo_da_carteira_do_usuario(gabriel, leilao):
    gabriel.propor_lance(leilao, 50)
    assert gabriel.carteira == 50.0


def test_quando_propor_um_lance_maior_que_o_saldo_da_carteira_nao_deve_permitir_o_lance(gabriel, leilao):
    with pytest.raises(LanceInvalido):
        gabriel.propor_lance(leilao, 150)
