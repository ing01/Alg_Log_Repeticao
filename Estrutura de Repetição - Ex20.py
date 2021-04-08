##Foi feita uma pesquisa com as crianças de uma determinada localidade. Faça um programa que: 
##leia o número de crianças nascidas no período; identifique o sexo (M ou F) e a idade da criança.
##O programa deve calcular e mostrar: a percentagem de crianças do sexo marculino; a percentagem de crianças do sexo feminino; a percentagem de crianças menores que 24 meses.

total_meninos = 0
total_meninas = 0
menor_que_24_meses = 0
maior_que_24_meses = 0
periodo = int (input('Digite o número de crianças nascidas no período: '))
for i in range (0, 5):
  sexo_crianca = input('Digite o sexo da criança (M para masculino e F para feminino): ')
  idade_crianca = int (input('Digite a idade da criança: '))
  if sexo_crianca == 'M' or sexo_crianca == 'm':
    total_meninos += 1
  elif sexo_crianca == 'F' or sexo_crianca == 'f':
    total_meninas += 1
  if idade_crianca < 2:
    menor_que_24_meses = idade_crianca
    menor_que_24_meses += 1
  else:
    maior_que_24_meses = idade_crianca
    maior_que_24_meses += 1
porcentagem_meninos = total_meninos / periodo * 100
porcentagem_meninas = total_meninas / periodo * 100
porcentagem_menores = menor_que_24_meses / periodo * 100
print('A porcentagem de meninos é de',porcentagem_meninos,'porcento.')
print('A porcentagem de meninas é de',porcentagem_meninas,'porcento.')
print('A porcentagem de crianças menores que 2 anos é de',porcentagem_menores,'porcento.')
