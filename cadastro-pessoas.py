# Algoritmo que registra as pessoas, usando como critério de parada a letra 'n'.
# Para identificar o perfil dos compradores numa loja de roupas e apresente como resultado a:
# quantidade de mulheres e de homens; quantidade de mulheres e de homens abaixo e acima de 18 anos; quantidade de mulheres e de homens acima de 60 anos.

mulheres = 0
homens = 0
mulher_adult = 0
mulher_jovem = 0
homem_adult = 0
homem_jovem = 0
mulher_idosa = 0
homem_idoso = 0
reg = str (input('Deseja cadastrar um comprador? S - Sim / N - Não ' ))
while reg == 's' or reg == 'S':
  sexo = str (input('Digite o sexo do comprador (F para Feminino ou M para Masculino): '))
  idade = int (input('Digite a idade do comprador: '))
  if sexo == 'M' or sexo == 'm':
    homens += 1
    if idade < 18:
      homem_jovem += 1
    elif idade >= 18 and idade <= 59:
      homem_adult += 1
    else:
      homem_idoso += 1
  if sexo == 'F' or sexo == 'f':
    mulheres += 1
    if idade < 18:
      mulher_jovem += 1
    elif idade  >= 18 and idade <= 59:
      mulher_adult += 1
    else:
      mulher_idosa += 1
  reg = str (input('Deseja cadastrar um comprador? S - Sim / N - Não ' ))

print('A quantidade de mulheres é: ',mulheres)
print('Mulheres abaixo dos 18 anos: ',mulher_jovem)
print('Mulheres acima dos 18 anos: ',mulher_adult)
print('Mulheres acima dos 60 anos: ',mulher_idosa)

print('A quantidade de homens é: ',homens)
print('Homens abaixo dos 18 anos: ',homem_jovem)
print('Homens acima dos 18 anos: ',homem_adult)
print('Homens acima dos 60 anos: ',homem_idoso)
