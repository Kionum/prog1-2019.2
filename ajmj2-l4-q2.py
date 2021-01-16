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
def verificaMesmoTipo(matriz1, matriz2):
    if len(matriz1) == len(matriz2):
        cont = 0
        for item1, item2 in matriz1, matriz2:
            if len(item1) != len(item2):
                return False
            cont += 1
        return True
    return False


def somaMesmoTipo(matriz1, matriz2):
    while len(matriz1) == len(matriz2):
        matrizSoma = []
        for item in range(len(matriz1)):
            linha = []
            for coisa in range(len(matriz1[0])):
                linha.append(matriz1[item][coisa]+matriz2[item][coisa])
            matrizSoma.append(linha)
        return matrizSoma


def main(matriz1, matriz2):
    verificacao = verificaMesmoTipo(matriz1, matriz2)
    if verificacao:
        print('A soma das matrizes é:', somaMesmoTipo(matriz1, matriz2))
    else:
        print('As matrizes são de tipos diferentes.')


'''[[1, 2, 3], [4, 5, 6]], [[7, 8, 9],[10, 11, 12]]'''

condicaoParada = True
while condicaoParada:
    matriz1 = []
    matriz1Input = True
    matriz2 = []
    matriz2Input = True
    matrizTemp = []
    matrizTemp2 = []
    while matriz1Input:
        valores = int(input('Matriz1 :Digite um valor para a matriz '))
        matrizTemp.append(valores)
        pulaLinhaInput = True
        while pulaLinhaInput:
            pulaLinha = input('Deseja terminar a linha?(s/n) ')
            if pulaLinha == 's':
                matriz1.append(matrizTemp)
                matrizTemp = []
                terminaMatrizInput = True
                while terminaMatrizInput:
                    terminaMatriz = input('Deseja terminar a matriz?(s/n) ')
                    if terminaMatriz == 's':
                        matriz1Input = False
                        pulaLinhaInput = False
                        terminaMatrizInput = False
                    elif terminaMatriz == 'n':
                        print('\n')
                        pulaLinhaInput = False
                        terminaMatrizInput = False
                    else:
                        print('Digite s ou n.')
            elif pulaLinha == 'n':
                pulaLinhaInput = False
            else:
                print('Digite s ou n.')
    print('A matriz 1 é:', matriz1)
    while matriz2Input:
        valores = int(input('Matriz2: Digite um valor para a matriz '))
        matrizTemp2.append(valores)
        pulaLinhaInput = True
        while pulaLinhaInput:
            pulaLinha = input('Deseja terminar a linha?(s/n) ')
            if pulaLinha == 's':
                matriz2.append(matrizTemp2)
                matrizTemp2 = []
                terminaMatrizInput = True
                while terminaMatrizInput:
                    terminaMatriz = input('Deseja terminar a matriz?(s/n) ')
                    if terminaMatriz == 's':
                        matriz2Input = False
                        pulaLinhaInput = False
                        terminaMatrizInput = False
                    elif terminaMatriz == 'n':
                        print( '\n' )
                        pulaLinhaInput = False
                        terminaMatrizInput = False
                    else :
                        print('Digite s ou n.')
            elif pulaLinha == 'n':
                pulaLinhaInput = False
            else:
                print('Digite s ou n.')
    print('A matriz 2 é:', matriz2)
    main(matriz1, matriz2)
    continua = input('Deseja continuar?(s/n) ')
    if continua == 's':
        condicaoParada = False
