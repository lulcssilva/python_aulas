'''
Autor: Luana
Data 07/06/2024
versão 1.0
descrição: estudo da estrutura de repetição WHILE
'''
#=========================================================
indice = 1
while indice < 6:
    print(indice)
    indice = indice + 1 #indice += 1

#=========================================================
print ('novo código')
idade = 33
while idade > 0 :
    print(idade)
    idade = idade -1
#=========================================================
print ('novo código')
indice_3 = 1
while True:
    print(indice_3)
    indice_3 = indice_3 + 1
    if indice_3 == 5:
        break
#=========================================================
print ('novo código')
while True:
    opcao = input('Digite S para finalizar o programa')
    if (opcao == 'S' or opcao =='s'):
        break