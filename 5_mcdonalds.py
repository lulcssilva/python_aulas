'''
Autor: Luana
Data 28/05/2024
versão 1.0
descrição: Escreva um algoritmo para exibir o nome do lanche de acordo com o número inserido pelo usuário,
            seguindo a tabela abaixo:
             
            nr. Lanche
            1   Big Mac
            2   Quarteirão
            3   McChicken
            4   Cheddar McMelt
            5   McFish
'''
#=========================================
#entrada
numero = 0
print('nr.Lanche \n 1.Big Mac \n 2.Quarteirão \n 3.McChicken \n 4.Cheddar McMelt \n 5.McFish')
lanche =int(input('Digite o número do lanche desejado'))
if lanche == 1:
   lanche_escolhido = '1.Big Mac'
elif lanche == 2:
     lanche_escolhido = '2.Quarteirão'
elif lanche == 3:
     lanche_escolhido = '3.McChicken'
elif lanche == 4:
     lanche_escolhido = '4. Cheddar McMelt'
elif lanche == 5:
     lanche_escolhido = '5.Mcfish'
else:
    lanche_escolhido = 'digite um número válido'

print('O lanche escolhido foi: ',  lanche_escolhido)
print('********************************************** ')