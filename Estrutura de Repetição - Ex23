##Faça um programa que leia um valor N inteiro e positivo
##Calcule e mostre o valor de E, conforme a fórmula: E =  1+11!+12!+13!+14!+...+1N!

N = int(input('Informe o valor de N: '))
E = 1
for fat in range(1,N+1): # fat = 1!   fat = 2!   fat = 3!   fat = 4!
    fatorial = 1
    contador = 1
    while contador <= fat:  # 1 * 1 = 1    1 * 2 = 2    2 * 3 = 6    6 * 4 = 24
        fatorial = fatorial * contador
        contador += 1 # contador = contador + 1
    divisao = 1 / fatorial
    E = E + divisao
print('E = ',E)
