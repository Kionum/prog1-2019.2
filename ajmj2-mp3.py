produtos = []
produtinhos = []
cont = 0
cont2 = 0
cont3 = (3*(cont)+1)
cont4 = (3*(cont)+2)
cont5 = (3*(cont)+3)
precoCont = ()
quantidadeTotalCont = ()
arq = open('estoque.txt', 'r')
lerLinhas = arq.readlines()
arq.close()
def processaLinha(linha):
    linhaNova = ''
    for caractere in linha:
        if caractere != '\n':
            linhaNova += caractere
    return linhaNova
for coisa in range (len(lerLinhas)):
    b = processaLinha(lerLinhas[cont2])
    produtinhos.append(b)
    cont2 += 1
for coisa in range (len(produtinhos)):
    item = produtinhos[cont3]
    quantidade = produtinhos[cont4]
    preco = produtinhos[cont5]
    cont += 1
    produto = (item, quantidade, preco)
    produtos.append(produto)
print(produto)
'''Não consegui terminar até o final do tempo'''
