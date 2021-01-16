vivo = 1  # vidas do personagem
x = 4  # posição do personagem eixo x
y = 2  # posição do personagem eixo y
escudo = 0  # escudos no inventário
escudoDisp = 1  # escudos disponíveis no cenário
escudoEquip = 0  # escudos equipados
varaDisponivel = 1  # varas disponíveis no cenário
varaPega = 0  # varas no inventário
varaEquip = 0  # varas equipadas
chaveBau = 0  # chaves do baú no inventário
chaveBauDisp = 1  # chaves do baú no cenário
chavePorta = 0  # chaves da porta no inventário
chavePortaDisp = 1  # chaves da porta disponíveis
equipamento = str()  # equipamento no inventário
print('Você acorda.\nVocê está num chão duro e frio, seu corpo dói, aparentemente você não está sangrando.')
print('Você consegue sentir um buraco à sua direita e escuta alguns grunhidos abafados vindos de fora.')
while vivo == 1:  # Os comando continuaram a ser rodados enquanto o personagem estiver vivo
    comando = input('digite seu comando. (andar/pegar/usar/abrir/equipar)\n')  # pede o comando ao usuário
    """if comando == 'test':
        print('x =', x, 'y = ', y) eu usei esse comando pra testar o lugar do personagem"""
    if comando == 'andar':  # comandos para andar
        direcao = input('para qual direção? cima/baixo/direita/esquerda\n')
        if direcao == 'cima':
            y += 1
            print('você anda pra cima')
        if direcao == 'baixo':
            y -= 1
            print('você anda pra baixo')
        if direcao == 'direita':
            x += 1
            print('você anda pra direita')
        if direcao == 'esquerda':
            x -= 1
            print('você anda pra esquerda')
    if x < 1 or y < 1 or x > 7 or y > 7:  # paredes
        print('Você bateu numa parede')
        if x <= 0:
            x = 1
        if x >= 8:
            x = 7
        if y <= 0:
            y = 1
        if y >= 8:
            y = 7
    if x == 3 and y == 6 or x == 4 and y == 6 or x == 5 and y == 6 or x == 5 and y == 5 or x == 5 and y == 4\
            or x == 4 and y == 4 or x == 3 and y == 4 or x == 3 and y == 5:  # mesa
        print('você bate numa mesa. A mesa está quebrada, aparentemente algo muito pesado (ou forte)'
              ' amassou a grossa perna de madeira de uma mesa aparentemente forte.')
        if direcao == 'cima':
            y -= 1
        if direcao == 'baixo':
            y += 1
        if direcao == 'direita':
            x -= 1
        if direcao == 'esquerda':
            x += 1
    if x == 6 and y == 1 or x == 7 and y == 1:  # objeto do cenário: pilha de ossos
        print('Tem uma pilha de ossos, nem todos são humanos, melhor não mexer')
        if direcao == 'baixo':
            y += 1
        if direcao == 'direita':
            x -= 1
    if x == 1 and y == 4 and escudoDisp == 1:  # objeto interativo: suporte de armas
        print('você vê um suporte de armas')
        if comando == 'usar':
            print('você vê várias pás, e armas em ruínas mas atrás de todo o entulho você acha um escudo.')
            interagir = input('Deseja pegar o escudo? s/n')
            if interagir == 's':
                escudo += 1
                escudoDisp -= 1
                print('você pega o escudo')
    if x == 5 and y == 2:  # buraco da morte
        print('você caiu num buraco, quebrou o pescoço e morreu, nossa que azar em meu amigo.')
        vivo -= 1
    if x == 1 and y == 1 and varaDisponivel == 1:  # vara no chão
        print('você pisou em algo\n é uma vara no chão!')
        if comando == 'pegar':
            varaPega += 1
            print('você pegou a vara')
            varaDisponivel -= 1
    if x == 7 and y == 2 and chaveBauDisp > 0:  # buraco na parede com chave do baú
        print('você vê um buraco na parede com alguma coisa brilhando')
        if comando == 'usar' and varaEquip >= 1:
            chaveBau += 1
            chaveBauDisp -= 1
            print('Você consegue alcançar o objeto com a vara, é uma chave prateada!')
        elif comando == 'usar':
            print('Você tenta alcançar o objeto mas ele está muito longe.')
    if x == 1 and y == 6 and chavePortaDisp > 0:  # baú com chave da porta
        print('Tem um baú com uma tranca prateada aqui')
        if comando == 'abrir' and chaveBau >= 1:
            print('você abre o baú e a chave prateada se quebra, você encontra algumas pedras e um pouco de carvão.')
            print('alguns trapos de roupa suja, tudo lixo. mas no fundo você vê uma chave dourada, você a pega')
            chavePorta += 1
            chaveBau -= 1
            chavePortaDisp -= 1
        elif comando == 'abrir':
            print('Está trancado.')
    if comando == 'equipar':  # comando de equipar
        if varaPega == 1 and escudo == 1:
            equipamento = str('escudo, vara')
        if varaEquip == 1 and escudoEquip == 1:
            equipamento = str()
        if varaEquip == 1 and escudo == 1:
            equipamento = str('Escudo')
        if escudoEquip == 1 and varaPega == 1:
            equipamento = str('Vara')
        elif varaPega == 1 and escudoDisp == 1:
            equipamento = str('vara')
        elif escudo == 1 and varaDisponivel == 1:
            equipamento = str('Escudo')
        equip = input(f'Oque deseja equipar?\n equipamentos disponíveis: {equipamento} ')
        if escudo == 1 and equip == 'escudo' and escudoEquip == 0:
            print('você equipou o escudo, +2 def')
            escudoEquip += 1
        if varaPega == 1 and equip == 'vara':
            print('você equipou a vara, +1 str, pode alcançar itens longe')
            varaEquip += 1
    if x == 7 and y == 6:  # porta final
        print('você vê uma porta de madeira grande, sem aberturas e sem frestas, o buraco da fechadura é dourado,')
        print('Mas você não consegue ver o outro lado.')
        if comando == 'abrir' and chavePorta == 1:
            print('Você abre a porta')
            vivo += 1
        elif comando == 'abrir':
            print('está trancada')
if vivo > 1:  # final
    print('Um orc brutamontes que estava apoiado cai, então isso que tampava a fechadura.')
    print('Vários orcs com uniformes olham para você. todos com uma expressão mais irritada do que surpresa.')
    print('Se prepare, você vai lutar.')
    # desculpa se vc realmente pensou que ia lutar eu n fiz essa parte não tira ponto por favor
if vivo < 1:
    print('Você morreu, tente novamente')
