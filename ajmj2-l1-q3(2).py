num1 = int(input('Primeiro número '))
if 0 <= num1 <= 100:
    pass
else:
    raise ValueError('Número deve ser entre 0 e 100.')
num2 = int(input('Segundo número '))
if 0 <= num2 <= 10:
    pass
else:
    raise ValueError('Número deve ser entre 0 e 10.')
print(f'{str(num1) + str(num2)}, {num1 + num2} e {float(num1 + (num2 / 10))}')
