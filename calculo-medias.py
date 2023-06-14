# Algoritmo que calcule e informe a média de idades de 5 alunos.

idade = 1
soma_numeros = 0
while idade < 6:
    aluno = int(input('Qual a idade do aluno? '))
    idade += 1
    soma_numeros = soma_numeros + aluno
    media = soma_numeros / 5
print('A média de idade entre os alunos é de',media,'anos.')
