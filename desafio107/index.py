import moeda

p = float(input('Digite o preço: R$ '))
t = int(input('Digite a taxa - em (%): '))

print(f'A metade de {p} é {moeda.metade(p)}.')
print(f'O dobro de {p} é {moeda.dobro(p)}.')
print(f'Aumentando {t}% de {p} temos, {moeda.aumentar(p, t)}.')
print(f'Reduzindo {t}% de {p} temos, {moeda.diminuir(p, t)}.')
