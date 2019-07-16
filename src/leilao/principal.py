from src.leilao.dominio import Usuario, Lance, Leilao
gabriel = Usuario("Gabriel")
gustavo = Usuario("Gustavo")

lance1 = Lance(gabriel, 200.0)
lance2 = Lance(gustavo, 100.0)

leilao = Leilao("leilao de celular")
leilao.lances.append(lance2)
leilao.lances.append(lance1)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')


avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'Maior Lance: {avaliador.maior_lance}')
print(f'Menor Lance: {avaliador.menor_lance}')
