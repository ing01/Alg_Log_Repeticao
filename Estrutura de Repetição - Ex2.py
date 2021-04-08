##Faça um algoritmo que mostre o cumprimento ‘Olá ‘ para o nome de alguém (4 pessoas). Exemplo ‘Olá Mariana’.

qnome=1
while qnome <= 4:
    nome = input('Qual seu nome? ')
    print('Olá,',nome, end="\n")
    qnome = qnome + 1
