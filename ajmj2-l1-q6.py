print('olá eu sou uma calculadora para operações binárias!')
x = float(input('me diga seu primeiro valor\n'))
y = float(input('Agora o segundo valor\n'))
oper = input('qual tipo de operação deseja fazer? para: soma: +, subtração: -, multiplicação: *, divisão: /\n')
if oper == '+':
    print(f'A soma de {x} com {y} vale {x + y}')
    exit()
if oper == '-':
    print(f'A subtração de {x} por {y} vale {x - y}')
    exit()
if oper == '*':
    print(f'A multiplicação de {x} por {y} vale {x * y}')
    exit()
if oper == '/':
    print(f'A divisão de {x} por {y} vale {x / y}')
    exit()
else:
    exit('Entrada não válida.')