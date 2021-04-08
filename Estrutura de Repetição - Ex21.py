##Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
##valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

for valor in range (1):
  divida = float (input('Digite o valor da dívida: '))
if divida <= 1099:
  print('Esse valor não conta com juros.')
  print('Quantidade de parcelas para quitação: 1.')
  print('Valor da parcela:',divida)
if divida >= 1100 and divida <= 1149:
  parcela = divida / 3
  print('O valor de juros dessa dívida é de 100 reais.')
  print('Quantidade de parcelas para quitação: 3.')
  print('O valor da parcela:',parcela)
if divida >= 1150 and divida <= 1199:
  parcela = divida / 6
  print('O valor de juros dessa dívida é de 150 reais.')
  print('Quantidade de parcelas para quitação: 6.')
  print('O valor da parcela:',parcela)
if divida >= 1200 and divida <= 1249:
  parcela = divida / 9
  print('O valor de juros dessa dívida é de 200 reais.')
  print('Quantidade de parcelas para quitação: 9.')
  print('O valor da parcela:',parcela)
if divida >= 1250:
  parcela = divida / 12
  print('O valor de juros dessa dívida é de 250 reais.')
  print('Quantidade de parcelas para quitação: 12.')
  print('O valor da parcela:',parcela)
