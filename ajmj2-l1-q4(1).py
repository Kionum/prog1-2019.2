hora1 = int(input('Primeira hora '))
hora2 = int(input('Segunda hora '))
hora3 = int(input('Terceira hora '))
if hora1 is hora2 or hora1 is hora3 or hora2 is hora3:  # eu não sabia que is e or existiam quando fiz o resto.
    raise ValueError('Existem horas iguais.')
else:
    pass
if -1 <= hora1 <= 24:
    pass
else:
    raise ValueError('horas tem que estar entre 0 e 24')
if -1 <= hora2 <= 24:
    pass
else:
    raise ValueError('Horas devem ser entre 0 e 24')
if -1 <= hora3 <= 24:
    pass
else:
    raise ValueError('Horas devem estar entre 0 e 24')
if hora1 <= hora2 <= hora3:
    print(f'Marquinhos entrou às {hora1}, Marquinhos sairá às {hora2} e a lotérica fecha às {hora3}')
else:
    if hora2 <= hora3 <= hora1:
        print(f'Marquinhos entrou às {hora2}, Marquinhos sairá às {hora3} e a lotérica fecha às {hora1}')
    else:
        if hora3 <= hora2 <= hora1:
            print(f'Marquinhos entrou às {hora3}, Marquinhos sairá às {hora2} e a lotérica fecha às {hora1}')
        else:
            if hora1 <= hora3 <= hora2:
                print(f'Marquinhos entrou às {hora1}, Marquinhos sairá às {hora3} e a lotérica fecha às {hora2}')
            else:
                if hora2 <= hora1 <= hora3:
                    print(f'Marquinhos entrou às {hora2}, Marquinhos sairá às {hora1} e a lotérica fecha às {hora3}')
                else:
                    if hora3 <= hora1 <= hora2:
                        print(f'Marquinhos entra às {hora3}, Marquinhos saiu às {hora1} e a lotérica fecha às {hora2}')
                    else:
                        raise ValueError
