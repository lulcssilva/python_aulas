'''
Autor: Luana 
Data 04/06/2024
versão 1.0
descrição: "Classificação de idade"
  Escreva um programa que leia a idade de um individuo e escreva a faixa etária a que pertence, 
  de acordo com a tabela abaixo:
  faixa Etária        Classificação
    <12                 Criança
    13~17               Adolescente
    18~59               Adulto
    >60                 idoso

'''
idade = 0
classificacao =''
idade = int(input('Digite a sua idade e descubra a sua classificação'))
if idade >=0 and idade <= 12:
   classificacao = 'Criança'
elif idade >= 13 and idade <= 17:
    classificacao = 'Adolescente'
elif idade >= 18 and idade <= 59:
     classificacao = 'Adulto'
elif idade > 59: 
     classificacao = 'idoso'
else:
     classificacao = 'Idade inserida inválida'
print(classificacao)

