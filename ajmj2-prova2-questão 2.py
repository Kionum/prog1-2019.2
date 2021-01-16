def retornaDicionarioQ(string):
    dic = {}
    listaCaracteres = []
    lista2 = []
    for caractere in string:
        listaCaracteres.append(caractere)
    for caractere in listaCaracteres:
        temp = caractere
        cont = 0
        for item in listaCaracteres:
            if item == caractere:
                cont += 1
        listaTemp = [caractere, cont]
        lista2.append(listaTemp)
    for coisa in lista2:
        dic[coisa[0]] = coisa[1]
    return dic
        
    
print(retornaDicionarioQ(input('Digite a mensagem. ')))
