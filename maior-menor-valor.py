# Algoritmo que recebe o valor de 20 preços de TV, determina e apresenta o valor mais caro e mais barato.

cont = 1
while cont <= 10:
    modelo = input('Informe o modelo da TV: ')
    preco = float(input('Informe o preço: '))
    if cont == 1:
        alto = preco
        nome_alto = modelo
        baixo = preco
        nome_b = modelo
    elif preco >= alto:
        alto = preco
        nome_alto = modelo
    elif preco <= baixo:
        baixo = preco
        nome_b = modelo
    cont = cont + 1
print('A TV',nome_alto,' é mais cara com',alto,'reais')
print('A TV',nome_b,' é mais barata com',baixo,'reais')
