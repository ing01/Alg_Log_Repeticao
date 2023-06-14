# Algoritmo que recebe 23 números, calcule e exiba a quantidade de números pares e impares.

qpar = 0
qimpar = 0
for cont in range(1,24):
  num = float(input('Digite um número: '))
  if num%2 == 0:
    qpar = qpar + 1
  else:
    qimpar = qimpar + 1
print('Quantidade de números pares: ', qpar)
print('Quantidade de números ímpares: ', qimpar)
