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
alunosAdicionar = []
alunos = []
def escreveNoArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'w')
    for aluno in alunos:
        arquivo.write(f'{aluno[0]}, {aluno[1]}, {aluno[2]}\n')

def adicionaAlunos(nomeArquivo):
    nome = input('Nome: ')
    nota = float(input('Nota: '))
    faltas = int(input('Faltas: '))
    estudante = (nome, nota, faltas)
    alunos.append(estudante)
    continua = input('Deseja continuar? s/n')
    if continua == 's':
        adicionaAlunos(nomeArquivo)


def excluiAlunos(alunoExcluir):
    for aluno in alunos:
        if alunoExcluir == aluno[0]:
            alunos.remove(aluno)


def adicionaFaltas(aluno, faltas):
    for estudante in alunos:
        if aluno == estudante[0]:
            int(aluno[2])
            aluno[2] += faltas


def geraRelatorio(disciplina):
    print('Disciplina: ', disciplina)
    for aluno in alunos:
        print(f'Aluno: {aluno[0]}\nNota: {aluno[1]}\nFaltas: {aluno[2]}')


def preparaArquivo(nomeArquivo):
    try:
        abreArquivo = open(nomeArquivo, "r")
    except IOError:
        abreArquivo = open(nomeArquivo, 'w')
        abreArquivo.close()
        abreArquivo = open(nomeArquivo, 'r')
    arquivo = abreArquivo.readlines()
    for linha in arquivo:
        aluno = []
        temp = ''
        for caractere in linha:
            if caractere == ',':
                aluno.append(temp)
            elif caractere == '\n':
                alunos.append(aluno)
            else:
                temp += caractere
    abreArquivo.close()


def main():
    arquivo = input('Digite o nome do arquivo (padrão: <nome_da_disciplina-ano-semestre.txt>): ')
    preparaArquivo(arquivo)
    menu = input('O que deseja fazer?\nAdicionar Aluno(1)\nExcluir aluno(2)\nAdicionar Faltas(3)\nGerar relatório(4)')
    if menu == '1':
        adicionaAlunos(arquivo)
    if menu == '2':
        alunoExcluir = input('Que aluno deve ser excluído? ')
        excluiAlunos(alunoExcluir)
    if menu == '3':
        alunoFaltas = input('Que aluno vai levar falta? ')
        faltasAluno = int(input('Quantas faltas serão adicionadas?'))
        adicionaFaltas(alunoFaltas, faltasAluno)
    if menu == 4:
        disciplina = input('Qual a disciplina pro relatório? ')
        geraRelatorio(disciplina,)
    continuar = input('Deseja continuar? (s/n)')
    escreveNoArquivo(arquivo)
    if continuar == 's':
        main()


main()
