##Elabore um algoritmo que informada a idade de 10 nadadores o mesmo terá condições de classificar em uma das seguintes categorias: 
##infantil = 5 - 10 anos; juvenil = 11-17 anos; adulto >= maiores de 18 anos.

for nadador in range(10):
  idade = int (input('Qual a idade do nadador? '))
  if idade < 5:
    print('O nadador não tem idade para se classificar nas categorias.')
  if idade >= 5 and idade <= 10:
    print('Se classifica na categoria Infantil.')
  if idade >= 11 and idade <= 17:
    print('Se classifica na categoria Juvenil.')
  else:
    if idade >= 18:
      print('Se classifica na categoria Adulto.')
