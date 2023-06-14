# Algoritmo que calcula a média aritmética de preços de 5 produtos.

soma_numeros = 0
for produto in range(1, 6):
    produto = float(input('Qual o valor do produto? '))
    produto += 1
    soma_numeros = soma_numeros + produto
    media = soma_numeros / 5
print('A média aritmética de preços é de R$',media)
