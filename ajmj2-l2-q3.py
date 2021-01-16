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
calculadora = 2  # variável que checa se a calculadora ainda deve rodar
while calculadora > 1:  # vai parar a calculadora se a variável for 1 ou menor
    priValor = float(input('me diga seu primeiro valor\n'))  # pede o primeiro valor
    operador = input('qual tipo de operação deseja fazer?\n')  # pede o operador a ser usado
    if operador == '!':  # se o operador for fatorial, calcula e pergunta se quer fazer outra operação
        fatorial = 1
        n = 2
        while n <= priValor:
            fatorial = fatorial * n
            n = n + 1
        print(f'{priValor}!=', fatorial)
        calculadora -= 1
        print(calculadora)
    if operador != '!':  # só continua para as outras operações se não for fatorial.
        segValor = float(input('Agora o segundo valor\n'))  # pede o segundo valor
        resultado = float(0)  # variável para os resultados
        if operador == '+':  # se o operador for "*"
            print(priValor, operador, segValor, '=', priValor + segValor)  # realiza soma
            calculadora -= 1
        if operador == '-':  # se o operador for "-"
            print(priValor, operador, segValor, '=', priValor - segValor)  # realiza subtração
            calculadora -= 1
        if operador == '*':  # se o operador for *
            cont = 0  # contador para o while
            while cont < segValor:  # enquanto contador for menor que o segundo valor
                resultado += priValor  # adiciona o primeiro valor ao resultado segValor vezes
                cont += 1  # adiciona +1 ao contador para pode parar quando chegar em segValor
            print(priValor, operador, segValor, '=', resultado)  # imprime o resultado
            calculadora -= 1
        if operador == '/':  # se o operador for "/"
            print(priValor, operador, segValor, '=', priValor / segValor)  # faz a divisão
            calculadora -= 1
        if operador == '//':  # se o operador for "//"
            cont = 0  # contador para o while
            while cont <= priValor:  # enquanto o contador for menor que o primeiro valor
                cont += segValor  # vai adicionar o segundo valor ao contador
                resultado += 1  # resultado vai contar quantas vezes essa "adição" aconteceu
            if cont > priValor:  # vai imprimir o resultado - 1 se o contador ficou maior que o primeiro valor
                print(priValor, operador, segValor, '=', resultado - 1)  # imprime o resultado - 1
                calculadora -= 1
            if cont == priValor:  # vai imprimir o resultado normalmente se a "divisão" foi exata
                print(priValor, operador, segValor, '=', resultado)  # imprime o resultado
                calculadora -= 1
        if operador == '%':
            resultado = priValor
            cont = 0
            while cont <= priValor:
                cont += segValor
                resultado += 1
            cont -= segValor
            print(priValor, operador, segValor, '=', priValor - cont)
            calculadora -= 1
        if operador == '**':
            print(priValor, operador, segValor, '=', priValor ** segValor)  # realiza e imprime potenciação
            calculadora -= 1
    while calculadora == 1:
        pergunta = input('Deseja fazer uma nova operação? s/n ')
        if pergunta == 's':
            calculadora += 1
            print(calculadora)
        if pergunta == 'n':
            calculadora -= 1
            print('Adeus')
