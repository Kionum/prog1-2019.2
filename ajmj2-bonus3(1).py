print('Os arquivos "lista4questao4Arquivo1.txt" e "lista4questao4Arquivo2.txt" devem estar na mesma pasta que o programa. Se estão, desconsiderar.')
def tiraEspaco(string):
    novaLista = []
    temp1 = ''
    for valor in string:
        if valor != ' ':
            temp1 += valor
        if valor == ' ':
            temp1
            novaLista.append(temp1)
            temp1 = ''
    return novaLista
def checaPrimo(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    temp2 = 3
    while temp2 * temp2 <= num:
        if num % temp2 == 0:
            return False
        temp2 += 2
    return True
def processaArquivo(arquivo):
    processaArquivos = tiraEspaco(arquivo)
    for numero in processaArquivos:
        temp3 = int(numero)
        checagemPrimo = checaPrimo(temp3)
        if checagemPrimo:
            if arquivo == lerArquivo1:
                temp4 = str(temp3)
                arquivo3.write(temp4)
                arquivo3.write(' ')
            if arquivo == lerArquivo2:
                temp4 = str(temp3)
                arquivo4.write(temp4)
                arquivo4.write(' ')
arquivo1 = open('lista4questao4Arquivo1.txt', 'r')
arquivo2 = open('lista4questao4Arquivo2.txt', 'r')
arquivo3 = open('lista4questao4resultadoArquivo1.txt','w')
arquivo4 = open('lista4questao4resultadoArquivo2.txt','w')
lerArquivo1 = arquivo1.readline()
arquivo1.close()
lerArquivo2 = arquivo2.readline()
arquivo2.close()
processaArquivo(lerArquivo1)
arquivo3.close()
processaArquivo(lerArquivo2)
arquivo4.close()
