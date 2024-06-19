'''
Autor: Luana 
Data: 13/06/2024
Versão: 1.0
Descrição:Faça um programa que receba o número da chamada dos alunos do curso de python no periodo noturno do senai 115 e apresente o seu nome.
'''


aluno_python_senai =['Luana','Gustavo','Danielle', 'Felipe','João', 'Thiago','Vitor','José','Arthur','Pedro', 'Mauricio',
                     'Davi','Kawan','Andrey','Lucas','Diego','João2','Ana','vinicius','Adriel','Patrick','Bruno','Professor Girafalles mini']
while True:
    nr_chamada = 0
    nr_chamada = int(input('digite o número da chamada desejado'))
    print(aluno_python_senai[nr_chamada])

    continuar = input('Digite S para sair ou C para Continuar')
    if continuar == 'S':
        break