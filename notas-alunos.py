# Algoritmo que recebe duas notas de seis alunos. Calcule e mostre: a média aritmética das duas notas de cada aluno;
# Até 3 = Reprovado
# Entre 3 e 7 = Exame
# De 7 para cima = Aprovado

# Deve mostrar: o total de alunos aprovados; o total de alunos de exame; o total de alunos reprovados; a média da classe.

reprovado = 0
exame = 0
aprovado = 0
soma = 0
for contador in range (0, 6):
  nota1 = int (input('Informe a primeira nota: '))
  nota2 = int (input('Informe a segunda nota: '))
  media = (nota1 + nota2) / 2
  if media < 3:
    print('Reprovado.')
    reprovado = reprovado + 1
  elif media >= 3 and media <= 7:
    print('Exame.')
    exame = exame + 1
  elif media > 7:
    print('Aprovado.')
    aprovado = aprovado + 1
soma = media + soma
print('Total de alunos aprovados: ',aprovado)
print('Total de alunos reprovados: ',reprovado)
print('Total de alunos com exame: ',exame)
print('Média total da classe: ',media)
