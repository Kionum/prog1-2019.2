def novaLista():
    listaNova = []
    continuar = True
    while continuar:
        adicionar_numero = int(input('Digite um número para ser adicionado à lista'))
        listaNova.append(adicionar_numero)
        escolha2 = input('Deseja continuar? s/n')
        if escolha2 == 'n':
            continuar = False
    return listaNova

def maior_numero(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maior_num = maior_numero(lista[1:])
        if maior_num > lista[0]:
            return maior_num
        else:
            return lista[0]


escolha1 = input('Deseja usar a lista pronta(1) ou fazer sua própria?(2)')
if escolha1 == '1':
    print('O maior numero é:', maior_numero(
        [4, 4, 1, 6, 3, 9, 7, 4, 1, 0, 455, 125, 753, 4753, 345, 124, 999, 452, 6522, 754, 13542, 3442, 53234, 2354]))
elif escolha1 == '2':
    listaUsuario = novaLista()
    print('O maior número é:', maior_numero(listaUsuario))
