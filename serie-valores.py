# Algoritmo que recebe o número de termos, determine e mostre os valores de acordo com a série a seguir: 
# Série = 2, 7, 3, 4, 21, 12, 8, 63, 48, 16, 189, 192, 32, 567, 768...

numero_de_termos = int (input('Determine um numero de contagem para os termos '))
termo1 = 2
termo2 = 7
termo3 = 3
print(termo1, termo2, termo3)
termo_atual = 4
while termo_atual <= numero_de_termos:  
    termo1 = termo1 * 2
    print(termo1)
    termo_atual += 1    
    if termo_atual <= numero_de_termos:
        termo2 = termo2 * 3
        print(termo2)
        termo_atual += 1
        if termo_atual <= numero_de_termos:
            termo3 = termo3 * 4
            print(termo3)
            termo_atual += 1
