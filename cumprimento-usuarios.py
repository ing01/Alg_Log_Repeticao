# Algoritmo que receba quatro nomes e cumprimente com ‘Olá, x‘.

qnome=1
while qnome <= 4:
    nome = input('Qual seu nome? ')
    print('Olá,',nome, end="\n")
    qnome = qnome + 1
