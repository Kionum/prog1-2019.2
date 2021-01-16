def processaLinha(linha):
    linhaNova = ''
    for caractere in linha:
        if caractere != '\n':
            linhaNova += caractere
        else:
            return linhaNova

def reescreveArquivo(nomeArquivo, linhas):
    arquivo = open(nomeArquivo, 'w')
    for linha in linhas:
        arquivo.write(linha+'\n')
def removeDoArquivo(stringArquivo, stringParaRemover):
    linhas = []
    contRemovidas = 0
    abreArquivo = open(stringArquivo, 'r')
    arquivo = abreArquivo.readlines()
    abreArquivo.close()
    for linha in arquivo:
        novaLinha = processaLinha(linha)
        linhas.append(novaLinha)
    for item in linhas:
        if stringParaRemover == item:
            contRemovidas += 1
            linhas.remove(item)
    reescreveArquivo(stringArquivo, linhas)
    print(contRemovidas, 'linhas foram excluídas.')
def PerguntaUsuário():
    nomeArquivo = input('Digite o nome do arquivo. ')
    linhaRemover = input('Digite a linha a ser removida. ')
    removeDoArquivo(nomeArquivo, linhaRemover)

PerguntaUsuário()
        
    
