import moeda

p = float(input('Digite o preço: R$ '))
t = int(input('Digite a taxa - em (%): '))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.')
print(f'Aumentando {t}% de {moeda.moeda(p)} temos, {moeda.aumentar(p, t, True)}.')
print(f'Reduzindo {t}% de {moeda.moeda(p)} temos, {moeda.diminuir(p, t, True)}.')
