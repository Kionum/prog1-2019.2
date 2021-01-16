def calculaProdutoMatrizes(matriz1, matriz2):
    m3 = []
    if len(matriz2[0]) != len(matriz1):
        return [[]]
    else:
        for item in range(len(matriz1)):
            mult = (matriz1[item][item]) * (matriz2[item][item])
            m3.append(mult)
            print(m3)
        return m3
print(calculaProdutoMatrizes([[1,2],[3,4]],[[-1,3],[4,2]]))
