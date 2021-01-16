def tiraBarraEne(linha):
    linhaNova = ''
    for coisa in linha:
        if coisa != '\n':
            linhaNova += coisa
        else:
            return linhaNova
def removeDoArquivo(str1, str2):
    arquivo = open(str1, 'r')
    leArquivo = arquivo.readlines()
    arquivo.close
    novasLinhas = []
    cont1 = 0
    cont2 = 0
    contLinhas = 0
    for linha in leArquivo:
        novaLinha = tiraBarraEne(linha)
        novasLinhas.append(novaLinha)
    for linha in novasLinhas:
        if linha == str2:
            cont1 += 1
    for linha in novasLinhas:
        contLinhas += 1
        if str2 == linha:
            cont2 += 1
        if str2 == linha and cont1 == cont2:
            novasLinhas.remove(linha)
            arquivo = open(str1, 'w')
            for linha in novasLinhas:
                arquivo.write(linha+'\n')
            return contLinhas
    return -1
inputArquivo = input('Digite o nome do arquivo: ')
perguntaArquivo = input('O arquivo já existe? s/n ')
if perguntaArquivo == 'n':
     print('Crie um arquivo com linhas para serem analizadas.')
else:
    linhaInput = input('Que linha será removida? ')
    print(removeDoArquivo(inputArquivo, linhaInput))
