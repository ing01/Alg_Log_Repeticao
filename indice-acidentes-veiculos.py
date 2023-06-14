# Algoritmo que recebe nomes de cincocidades, número de veículos e acidentes para determinar:
# o maior índice de acidentes de trânsito e a que cidades pertence; o menor índice de acidentes de trânsito e a que cidades pertence; 
# qual é a média de veículos nas cinco cidades juntas; qual é a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

total_cidades = 5
somatoria_veiculos_cidades = 0
somatoria_acidentes_cidades_2000_veiculos = 0
numero_cidades_2000_veiculos = 0
for cidade in range(total_cidades):
  nome_cidade = (input('Digite o nome da cidade '))
  numero_veiculos = int (input('Digite o numero de veiculos '))
  numero_acidentes = int (input('Digite o numero de acidentes '))
  if cidade == 0:
        maior_casos_acidentes = numero_acidentes
        cidade_maior_casos_acidentes = nome_cidade
        menor_casos_acidentes = numero_acidentes
        cidade_menor_casos_acidentes = nome_cidade
  else:
      if numero_acidentes > maior_casos_acidentes:
             maior_casos_acidentes = numero_acidentes
             cidade_maior_casos_acidentes = nome_cidade
      if numero_acidentes < menor_casos_acidentes:
             menor_caso_acidentes = numero_acidentes
             cidade_menor_casos_acidentes = nome_cidade
             somatoria_veiculos_cidades = somatoria_veiculos_cidades + numero_veiculos
  if numero_veiculos > 2000:
        somatoria_acidentes_cidades_2000_veiculos += numero_acidentes
        numero_cidades_2000_veiculos += 1
  media_carros_cidades = somatoria_veiculos_cidades / total_cidades
if numero_cidades_2000_veiculos == 0:
    print('Não foi informada nenhuma cidade com menos de 2000 veículos')
else:
    media_acidentes_cidade_2000_veiculos = soma_acidentes_cidades_veiculos / numero_cidades_2000_veiculos
    print('A media de acidentes nas 5 cidades é de',media_acidentes_cidade_2000_veiculos,'acidentes.')
print('A cidade com maior casos é',cidade_maior_casos_acidentes,'com', maior_casos_acidentes,'acidentes.')
print('A cidade com menor casos é',cidade_menor_casos_acidentes,'com', menor_casos_acidentes,'acidentes.')
print('A media de carros nas 5 cidades é de',media_carros_cidades,'veículos.')
