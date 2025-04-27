import moeda

p = float(input('Digite o preço: R$ '))
t = int(input('Digite a taxa - em (%): '))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
print(f'Aumentando {t}% de {moeda.moeda(p)} temos, {moeda.moeda(moeda.aumentar(p, t))}.')
print(f'Reduzindo {t}% de {moeda.moeda(p)} temos, {moeda.moeda(moeda.diminuir(p, t))}.')
