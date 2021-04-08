##Faça um programa que receba a idade e a altura de várias pessoas. Calcule e exiba a média das alturas das pessoas com mais de 20 anos. 
##Para encerrar a entrada de dados, digite uma idade negativa ou igual a zero.

idade = int(input('Informe uma idade - 0 ou idade negativa para sair: '))
soma_altura = 0
cont = 0
while idade > 0:    
    altura = float(input('Informe a altura: '))
    if idade > 20:
        soma_altura = soma_altura + altura
        cont += 1
    idade = int(input('Informe uma idade - 0 ou idade negativa para sair: '))
media_altura = soma_altura / cont
print ('A média de altura das pessoas com mais de 20 anos é: ', media_altura)
