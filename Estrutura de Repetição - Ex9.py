##Faça um algoritmo que conheça 4 valores diferentes, some-os e mostre o resultado.

cont = 1
soma_numeros = 0
while cont <= 4:
    num = int(input('Informe um número: '))
    soma_numeros = soma_numeros + num
    cont += 1
    print('Total: ',soma_numeros)
