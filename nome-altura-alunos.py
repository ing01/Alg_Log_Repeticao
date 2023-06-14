# Algoritmo que receba altura e nome de dez alunos. Mostra o aluno mais alto e mais baixo e seus respectivos nomes.

cont = 1
while cont <= 5:
    nome = input('Informe um nome: ')
    altura = float(input('Informe a altura: '))
    if cont == 1:
        alto = altura
        nome_alto = nome
        baixo = altura
        nome_b = nome
    elif altura >= alto:
        alto = altura
        nome_alto = nome
    elif altura <= baixo:
        baixo = altura
        nome_b = nome
    cont = cont + 1
print('Aluno',nome_alto,' é mais alto com',alto,'metros')
print('Aluno',nome_b,' é mais baixo com',baixo,'metros')
