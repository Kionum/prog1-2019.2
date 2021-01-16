import math  # Esse comando importará a biblioteca math, que adiciona funções matemáticas e constantes em python.

a = float(input('Valor cateto oposto '))  # Esse comando pede o valor do primeiro cateto ao usuário.
b = float(input('Valor cateto adjacente '))  # Esse comando pede o valor do segundo cateto ao usuário.
h = math.sqrt((a ** 2) + (b ** 2))  # Essa linha faz o cálculo para a hipotenusa.
print(f'A hipotenusa vale {h:.4}')  # Essa linha serve para mostrar o resultado da hipotenusa para o usuário.
# Esses comandos são algoritmos, pois são um conjunto de instruções a serem seguidas para chegar a um resultado.
