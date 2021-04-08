##Faça um programa que receba: o preço unitário, a refrigeração (S para os produtos que necessitem de refrigeração e N para os que não necessitem)
##a categoria (A — alimentação; L — limpeza; e V — vestuário)
##Calcule e mostre: O custo de estocagem, O imposto calculado, A média dos valores adicionais, ou seja, a média dos custos de estocagem e dos impostos dos doze produtos.
##O maior preço final. O menor preço final. O total dos impostos. A quantidade de produtos com classificação barato. A quantidade de produtos com classificação caro.
##A quantidade de produtos com classificação normal.

total_de_produtos = 3 
total_de_produtos_baratos = 0
total_de_produtos_normais = 0
total_de_produtos_caros = 0
custo_de_estocagem = 0
total_de_custos_adicionais = 0
total_de_impostos_de_todos_os_produtos = 0
preco_do_produto_mais_caro  = 0
preco_final_do_produto = 0
preco_do_produto_mais_barato = 0

for produto in range(0,12):
    preco_do_produto = float (input('Insira o preço do produto: '))
    produto_necessita_de_refrigeracao = (input('Produto necessita de refrigeracao? (s/n) '))
    categoria_do_produto=(input('Digite a categoria do produto:  '))
    if preco_do_produto <= 20:
	    if categoria_do_produto == 'a':
		    custo_de_estocagem = 2
    if categoria_do_produto == '1':
        custo_de_estocagem = 3
        if categoria_do_produto == 'v':
            custo_de_estocagem = 4
    if preco_do_produto > 20 and preco_do_produto <= 50:
        if produto_necessita_de_refrigeracao == 's':
            custo_de_estocagem = 6
        else:
            custo_de_estocagem = 0
 
    if preco_do_produto > 50:
        if produto_necessita_de_refrigeracao == 's':
            if categoria_do_produto == 'a':
