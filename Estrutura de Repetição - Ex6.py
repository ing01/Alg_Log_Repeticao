##Faça um algoritmo que receba a idade de 10 pessoas, calcule e exiba a quantidade de pessoas maiores de idade, sendo que a maioridade é obtida após completar 18 anos.

qtde = 0
for cont in range(1,10):
  idade = int(input('Informe a idade: '))
  if idade >= 18:
    qtde = qtde + 1
print('Quantidade pessoas maiores de idade: ',qtde)
