##Faça um programa que receba um conjunto de valores inteiros, calcule e exiba o maior e o menor valor do conjunto.
##Para encerrar a entrada de dados, deve ser digitado o valor zero; Para valores negativos, deve ser enviada uma mensagem; 
##Esses valores (zero e negativos) não entrarão nos cálculos.

valor = int (input('Digite um valor inteiro e positivo: '))
maior = valor
menor = valor
while valor > 0:
  if valor > maior:
    maior = valor
  if valor < menor:
    menor = valor
  valor = int (input('Digite um valor inteiro e positivo: '))
  if valor < 0:
    print('Comando encerrado.')
print('O maior valor digitado foi',maior)
print('O menor valor digitado foi',menor)
