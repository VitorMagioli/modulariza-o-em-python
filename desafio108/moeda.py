def metade(n):
    return n/2

def dobro(n):
    return n*2

def aumentar(n, taxa):
    res = ((n*taxa)/100) + n
    return res

def diminuir(n, taxa):
    res= n - ((n*taxa)/100)
    return res
 
def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')