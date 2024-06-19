'''
Autor: Luana 
Data: 13/06/2024
Versão: 1.0
Descrição: Faça um programa que receba dois valores, sendo que o primeiro deve ser menor que o segundo.
    o programa deve apresentar todos os números impares contidos nesta sequência.
    (modulo % . exemplo 7%2=1)
'''
#variáveis
num_a = 0
num_b= 0

#Entrada
num_a = int(input('Digite o primeiro número: '))
num_b = int(input('Digite o segundo número'))
for nr_dentro_range in range(num_a, num_b):
   resto = nr_dentro_range %2
   #print(f'{nr_dentro_range} %2 = {resto}')
   if resto == 1:
      print(nr_dentro_range)