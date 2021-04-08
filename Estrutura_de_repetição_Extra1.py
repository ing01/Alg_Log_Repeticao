##Construir um algoritmo para calcular a média aritmética de um conjunto de valores inteiros positivos. Digitar zero para sair.

cont = 1
soma_numeros = 0
media = 0
while cont < 6:
  valor = int (input('Digite um valor inteiro e positivo OU digite 0 para sair : '))
  cont += 1
  if valor > 0:
    soma_numeros = soma_numeros + valor
  else:
    print('Valor não identificado.')
media = soma_numeros / 5
print('A média aritmética dos valor é', media)
