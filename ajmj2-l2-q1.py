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
print('Bem vindo(a), analisarei os números de 1 a 1000.')
a = int(input('Digite 1 para ímpares, 2 para pares e 3 para todos\n'))
cont = 0
contImpar = 1
while a == 3:
    cont += 1
    print(cont)
    if cont == 1000:
        a += 5
while a == 2:
    cont += 2
    print(cont)
    if cont == 1000:
        a += 5
while a == 1:
    contImpar += 2
    print(contImpar)
    if contImpar == 999:
        a += 5
