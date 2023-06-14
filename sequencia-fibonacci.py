# Algoritmo que monta os oito primeiros termos da sequência de Fibonacci.

numero_de_elementos_da_sequencia = 8
elementoN = 0
elementoNmais1 = 1
print(elementoN)
print(elementoNmais1)
for elemento in range(0, numero_de_elementos_da_sequencia):
    valor_do_fibonacci_atual = elementoN + elementoNmais1
    print('O valor atual da sequência fibonacci é de: ',valor_do_fibonacci_atual)
    elementoN = elementoNmais1
    elementoNmais1 = valor_do_fibonacci_atual
