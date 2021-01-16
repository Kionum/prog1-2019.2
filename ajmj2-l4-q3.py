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
def calculaTudo(quantidade, valor, imposto1, imposto2):
    totalSemImposto = quantidade * valor
    totalComImposto = totalSemImposto + (((totalSemImposto * imposto1) / 100) + ((totalSemImposto * imposto2 / 100)))
    return totalComImposto


def escreveNoArquivo(quantidade, valor, imposto1, imposto2, valorTotal, pagamento):
    try:
        arquivo = open("Sanduiches Jean.txt", "a+")
    except IOError:
        arquivo = open("Sanduiches Jean.txt", 'w')
    arquivo.write(f'Quantidade:     {quantidade}\n'
                  f'Valor:      {valor}\n'
                  f'Imposto Estadual: {imposto1}\n'
                  f'Imposto Federal: {imposto2}\n'
                  f'Forma de Pagamento:     {pagamento}\n'
                  f'Total:      {valorTotal}\n'
                  f'---------------------------------------------------------\n')
    arquivo.close()

def main():
    quantidade = int(input('Quantos sanduíches foram vendidos? '))
    valor = float(input('Qual é o valor do sanduíche? '))
    impostoEst = float(input('De quantos % é o imposto estadual? '))
    impostoFed = float(input('De quantos % é o imposto federal? '))
    pagamento = input('Como foi realizado o pagamento? Cartão de crédito/débito/A vista ')
    escreveNoArquivo(quantidade, valor, impostoEst, impostoFed, (calculaTudo(quantidade, valor, impostoEst, impostoFed)), pagamento)
    continua = input('Impresso! Deseja fazer outra operação? (s/n) ')
    if continua == 's':
        main()


main()