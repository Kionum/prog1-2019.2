"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1
Autor: Adriel José de Moraes Jordão (ajmj2)
Email: ajmj2@cin.ufpe.br
Data: 2019-08-23
Copyright(c) 2019 Adriel José de Moraes Jordão
"""
pares = []
def leArquivo():  # lê ou cria o arquivo para os números, além de processar as linhas e fazer os pares dos números.
    try:
        abreArquivo = open("arquivo binarios.txt", "r")
    except IOError:
        abreArquivo = open("arquivo binarios.txt", 'w')
    arquivo = abreArquivo.readlines()
    abreArquivo.close()
    if len(arquivo) >= 2:
        novasLinhas = []
        def processaLinhas(linha):
            temp = ''
            for caractere in linha:
                if caractere == '\n':
                    return temp
                else:
                    temp += caractere
        for linha in arquivo:
            novaLinha = processaLinhas(linha)
            novasLinhas.append(novaLinha)
        listaDecimal = []
        listaBinario = []
        cont = 0
        cont2 = 0
        listaBinario.append(novasLinhas[0])
        while cont2 < (len(novasLinhas) // 2):
            listaBinario.append(novasLinhas[2 * cont2])
            listaDecimal.append(novasLinhas[2 * cont2 + 1])
            cont2 += 1
        for item in range(len(listaDecimal)):
            listaTemp = [listaBinario[0 + cont], listaDecimal[0 + cont]]
            cont += 1
            pares.append(listaTemp)


def procuraArquivo(num, trueOrFalse):  # procura se a conversão já foi feita no arquivo antes.
    leArquivo()
    if trueOrFalse:
        for numero in pares:
            if numero[0] == str(num):
                return True
    elif not trueOrFalse:
        for numero in pares:
            if numero[1] == str(num):
                return True
    return False


def retornaDoArquivo(num, trueOrFalse):  # se a conversão já foi feita, retorna-a
    if trueOrFalse:
        for numero in pares:
            if numero[0] == num:
                return numero[1]
    elif not trueOrFalse:
        for numero in pares:
            if numero[1] == str(num):
                return numero[0]


def converteNumeros(num, trueOrFalse):  # Se a conversão nunca foi feita, converte o número
    if trueOrFalse:
        conversao = 0
        temp = str(num)
        cont = len(temp)
        for numero in temp:
            somaConversao = int(numero) * (2 ** (len(temp) - cont))
            conversao += somaConversao
            cont -= 1
        escreveArquivo(num, conversao)
        return conversao
    else:
        conversao1 = ''
        temp = num
        while temp != 0:
            temp2 = temp % 2
            temp3 = temp // 2
            temp = temp3
            conversao1 += str(temp2)
        conversao2 = ''.join(reversed(conversao1))
        escreveArquivo(conversao2, num)
        return conversao2


def escreveArquivo(binario, decimal):  # se a conversão nunca foi feita, escreve no arquivo a nova conversão
    arquivo = open('arquivo binarios.txt', 'a')
    arquivo.write(f'{binario}\n{decimal}\n')
    arquivo.close()


def menuPrincipal():  # menu principal, conversa com o usuário.
    perguntaTipo = input('Que tipo de conversão será feita?\nBinário > Decimal (1)\nDecimal > Binário (2)\n')
    if perguntaTipo == '1':
        numeroParaConversao = input('Digite o número a ser convertido (Deve ser um número binário)\n')
        if numeroParaConversao == 0 or numeroParaConversao == 1:  # esses números estavam quebrando o código.
            print('A conversão é:', numeroParaConversao)
        checaArquivo = procuraArquivo(numeroParaConversao, True)
        if checaArquivo:
            print('A conversão é:', retornaDoArquivo(numeroParaConversao, True))
        else:
            print('A conversão é:', converteNumeros(numeroParaConversao, True))
    else:
        numeroParaConversao = int(input('Digite o número a ser convertido\n'))
        if numeroParaConversao == 0 or numeroParaConversao == 1:  # esses números estavam quebrando o código.
            print('A conversão é:', numeroParaConversao)
        else:
            checaArquivo = procuraArquivo(numeroParaConversao, False)
            if checaArquivo:
                print('A conversão é:', retornaDoArquivo(numeroParaConversao, False))
            else:
                print('A conversão é:', converteNumeros(numeroParaConversao, False))
    perguntaContinuar = input('Deseja fazer outra conversão? s/n ')
    if perguntaContinuar != 'n':
        menuPrincipal()


menuPrincipal()
