# Algoritmo que calcula e exiba o salário reajustado de dez funcionários de acordo com a seguinte regra: Salário até 300, reajuste de 50%; 
# Salários maiores que 300, reajuste de 30%.

fun = 1
for cont in range(10):
  salario = float(input('Insira o salário: '))
if salario <= 300:
  reajuste = salario * 50 / 100
else:
  reajuste = salario * 30 / 100
  novosalario = salario + reajuste
print('O novo salário será de R$', novosalario)
