'''
Autor: Luana
Data 11/06/2024
versão 1.0
Algoritmo "Média turma"
Descrição   : Faça um programa que receba duas notas de seis alunos. 
                Calcule e mostre:
            	A média aritmética das duas notas de cada aluno; e
            	A mensagem que está na tabela a seguir:
                    Média Aritmética	Mensagem
                    Até 3	            Reprovado 
                    Entre 4 e 7 	    Exame
                    De 8 para cima	    Aprovado
            	O total de alunos aprovados;
            	O total de alunos de exame;
            	O total de alunos reprovados;
            	A média da classe.
'''
aluno = 0
qtdAluno = 6
alunosAprovados = 0
alunosReprovados = 0
alunosExames = 0
media_classe = 0
media_final = 0
somaMedia = 0
while aluno < qtdAluno:
    aluno = aluno + 1
    nota_um = 0
    nota_dois = 0
    media = 0
    nome= input('insira o nome do aluno:')
    nota_um = float(input(f'Digite a Primeira nota do aluno {aluno}: '))
    nota_dois = float(input(f'Digite a segunda notado aluno {aluno}: '))
    media = (nota_um + nota_dois)/2
    somaMedia = somaMedia + media
    if (media>=0 and media <= 3):
        print('Aluno reprovado')
        alunosReprovados += 1
    elif(media >=4 and media <=7):
        print('Aluno em recuperação')
        alunosExames += 1
    elif(media >=8 and media <=10):
        print('Aprovado')       
        alunosAprovados += 1
    else:
        print('Digite um valor válido')
media_final = round((somaMedia / qtdAluno),2)
print(f'média final da turma: {media_final}')
print(f'Quantidade de alunos aprovados:{alunosAprovados}')
print(f'Quantidade de alunos em recuperação:{alunosExames}')
print(f'Quantidade de alunos reprovados: {alunosReprovados}')
