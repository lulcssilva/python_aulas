'''
Autor: Luana
Data 17/06/2024
versão 1.0
descrição: Estudo do tipo de dado ARRAY (Vetor)
'''
carros = ['VM']

carros.append('GM') # adiciona na última posição o valor indicado
carros.append('Ford')
carros.append('Fiat')
carros.append('Renault')

print(carros)

carros.remove('Ford') #remove item indicando o valor 
print(carros)

carros.pop(3) #remove item indicando o index
print(carros)

print(len(carros))# tamanho do vetor atual
carros.pop(len(carros)-1) #deleta sempre a última posição do array
print(carros)