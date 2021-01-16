kWh = float(input('Quantos kWh você gastou esse mês?\n'))
ins = input('O Tipo de instalação à ser checado? digite R para residencial, C para comercial ou I para industrial\n')
if ins == 'C':
    if kWh <= 1000:
        c = float(kWh * .55)
        print(f'{c}')
        exit()
    elif kWh > 1000:
        c = float(kWh * .60)
        print(f'{c}')
        exit()
if ins == 'R':
    if kWh <= 500:
        r = float(kWh * .4)
        print(f'{r}')
    elif kWh > 500:
        r = float(kWh * .65)
        print(f'{r}')
if ins == 'I':
    if kWh <= 5000:
        i = (kWh * .55)
    elif kWh > 500:
        i = (kWh * .6)
else:
    exit(f'{ins} não cabe em nenhuma das categorias, digite R para residencial, C para comercial ou I para industrial')
