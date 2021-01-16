"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1
Autor: Adriel José de Moraes Jordão (ajmj2)
Email: ajmj2@cin.ufpe.br
Data: 2019-08-23
Copyright(c) 2019 Adriel José de Moras Jordão
"""
caractere = input('analisarei seu caractere:')
numAscii = ord(caractere)
if 64 < numAscii < 91:
    print('Seu caractere é uma letra maiúscula.')
elif 96 < numAscii < 123:
    print('Seu caractere é uma letra minúscula.')
elif 47 < numAscii < 58:
    print('Seu caractere é um número.')
else:
    print('Caractere desconhecido')
