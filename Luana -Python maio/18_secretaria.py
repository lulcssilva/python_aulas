'''
Autor: Luana
Data 17/06/2024
versão 1.0
Descrição   : Faça um programa que adicione alunos ao sistema da escola 
              (array) ou remova um aluno especifico.
              Nesse sistema deve estar previsito um menu com três opções:
              #===================================
              Sistema SENAI
              1 - Adicionar aluno:
              2 - Remover aluno:
              3 - Apresentar alunos
              4 - Sair
              Insira a opção desejada: 
              #===================================   
              Adicionar aluno
              Insira o nome do aluno:
              #===================================   
              Remover aluno
              Insira o nome do aluno para ser removido:
              #===================================   
              Alunos no sistema
              ['João', 'Pedro','Luana']
              #===================================   
'''

nomes_aluno = ['João', 'Pedro','Luana']
nome_digitado = ''
while True: 
    nomes_aluno = str(input(' Sistema SENAI, 1 - Adicionar aluno: ,2 - Remover aluno: ,3 - Apresentar alunos: ,4 - Sair. Insira a opção desejada:'))
    if nomes_aluno == '1':
       nome_digitado = str(input('Digite o nome do aluno que será adicionado'))
       nomes_aluno.append(nome_digitado)
    elif nomes_aluno == '2':
         nome_digitado = str(input('Digite o nome do aluno que será removido'))
         nomes_aluno.remove(nome_digitado)
    elif nomes_aluno == '3':
        print(nomes_aluno)
    elif nomes_aluno == '4':
        break

   