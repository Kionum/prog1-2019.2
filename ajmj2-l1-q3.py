num = int(input('Me diga um número de até 3 dígitos e inverterei-o\n'))  # Entrada que pede o número ao usuário.
if num > 999 or num < 0:
    print('Apenas Números entre 0 e 999, por favor.')
    exit('Apenas Números entre 0 e 999, por favor.')
if num > 99:
    priNums = num // 10  # Dois primeiros números
    priNum = priNums // 10  # Primeiro número, separando dos dois primeiros números
    segNum = priNums % 10  # Segundo número, separando dos dois primeiros números
    ultNum = num % 10  # Último numero
    inverso = (ultNum *100) + (segNum * 10) + priNum
    print(f'O contrário de {num} é {inverso}')
    exit()
if num > 9:
    priNum = num // 10  # Primeiro número, separando dos primeiros números
    segNum = num % 10  # Segundo número, separando dos dois primeiros números
    inverso = (segNum * 10) + priNum
    print(f'O contrário de {num} é {inverso}')
    exit()
if num < 10:
    print(f'Isso é apenas o número {num}.')
    exit()
