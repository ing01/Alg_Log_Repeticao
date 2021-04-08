##Faça um programa para o curso de ADS (6 módulos) que calcule e apresente os seguintes itens: Quantidade de homens e mulheres de cada módulo; Média de idades de cada módulo;
##Quantidade de homens e mulheres do curso todo; Média de idades do curso todo. Este algoritmo utiliza DUAS estruturas de repetição.

homens_mod = 0
mulheres_mod = 0
media_idades_geral = 0
for modulo in range (1,7):
    print('Módulo ', modulo,'........')
    idade = int (input('Informe a idade: '))
    homens = 0
    mulheres = 0
    media_idades_mod = 0
    while idade > 0:
        media_idades_mod += idade
        sexo = input('Informe o sexo f/m: ')
        if sexo == 'f' or sexo == 'F':
          mulheres += 1
        elif sexo == 'm' or sexo == 'M':
          homens += 1
        idade = int(input('Informe a idade: '))
    media_idades_mod = media_idades_mod / (mulheres + homens)
    print('Quantidade de homens no módulo',modulo,'é de: ',homens)
    print('Quantidade de mulheres no módulo',modulo,'é de: ',mulheres)
    print('A média de idade do módulo',modulo,'é de: ',media_idades_mod)
    homens_mod += homens
    mulheres_mod += mulheres
    media_idades_geral += media_idades_mod
media_idades_geral = media_idades_geral / 6
print('Quantidade de homens no curso todo: ',homens_mod)
print('Quantidade de mulheres no curso todo: ',mulheres_mod)
print('Média geral de idades no curso todo: ',media_idades_geral)
