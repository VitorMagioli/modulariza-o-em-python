import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de R$ {p:.2f} é R$ {moeda.metade(p):.2f}.')
print(f'O dobro de R$ {p:.2f} é R$ {moeda.dobro(p):.2f}.')
print(f'Aumentando 10% de R$ {p:.2f} temos, R$ {moeda.aumentar(p):.2f}.')
print(f'Reduzindo 15% de R$ {p:.2f} temos, R$ {moeda.diminuir(p):.2f}.')
