a = float(input('Primeiro ponto do centro da circunferência\n'))
b = float(input('Segundo ponto do centro da circunferência\n'))
r = int(input('Raio da circunferência\n'))
x = float(input('Primeiro ponto x\n'))
y = float(input('Segundo ponto x\n'))
if (x - a) ** 2 + (y - b) ** 2 == r ** 2:
    print('Os pontos estão no círculo')
    exit()
elif (x - a) ** 2 + (y - b) ** 2 > r ** 2:
    print('Os pontos não estão no círculo.')
    exit()
