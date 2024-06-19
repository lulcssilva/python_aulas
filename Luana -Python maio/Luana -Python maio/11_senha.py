'''
Autor: Luana
Data 07/06/2024
versão 1.0
algoritmo: Senha
descrição:faça um programa que solicite para o usuário a senha de acesso ao sistema, ele terá no máximo 3 tentativas para inserir a correta 
cadastrada(senai115), caso passe desse limite uma mensagem de erro debe aparecer.
'''
senha ='' #var para receber a senha do usuário
senhaPadrao = 'senai115' #senha padrão do sistema
tentativas = 3

while True:   
    senha = input('Digite a senha para finalizar o acesso')
   
    if senha == senhaPadrao:
        print('Acesso Liberado!')
        break
    else:
        tentativas = tentativas - 1 #tentativas -= 1
        print('Senha incorreta, Você só possui mais: ', tentativas, 'tentativas')
    if tentativas <= 0:
        print('Sistema Bloqueado')
        break
   

      