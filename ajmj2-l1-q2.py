diaAtual = int(input('me dia o dia atual '))
mesAtual = int(input('me diga o mês atual. '))
anoAtual = int(input('me diga o ano atual. '))
diaUser = int(input('me diga seu dia de nascimento '))
mesUser = int(input('me diga seu mes de nascimento. '))
anoUser = int(input('me diga seu ano de nascimento. '))
idadeAno = anoAtual - anoUser
idadeMes = mesAtual - mesUser
idadeDia = diaAtual - diaUser
if idadeMes < 0:
    print(f' você tem {idadeAno - 1} anos, {idadeMes + 12} meses e {idadeDia} dias de idade')
else:
    print(f' você tem {idadeAno} anos, {idadeMes} meses e {idadeDia} dias de idade')
