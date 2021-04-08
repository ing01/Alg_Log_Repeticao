##Um funcionário de uma empresa recebe, anualmente, aumento salarial.
##Sabe-se que: Esse funcionário foi contratado em 2005, com salário inicial de R$ 1.000,00. Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial.
##A partir de 2007, os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
##Faça um programa que determine o salário atual desse funcionário.

ano_atual = int(input('Qual é o ano atual? '))
salarioinicio = 1000
percentual_ano = 0.015
aumentoano = salarioinicio * percentual_ano
salarioano = salarioinicio + aumentoano
if ano_atual < 2006:
    print('Funcionário não recebe aumento este ano.')
else:
    print('2006 - Novo salário é de R$',salarioano)
for ano in range (2007, ano_atual + 1):
            percentual_ano = percentual_ano * 2
            aumentoano = salarioano * percentual_ano
            salarioano = salarioano + aumentoano
            print('O salário do ano de',ano,'é de R$',salarioano)
