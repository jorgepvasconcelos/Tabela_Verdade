# calculos
def disjuncao(cl1, cl2, linhas):
    print('entrou na disjunção')
    r = []
    test(cl1, cl2)
    for c in range(0, linhas):
        if cl1[c] == 'F' and cl2[c] == 'F':
            r.append('F')
        else:
            r.append('V')
    cl1.clear()
    cl2.clear()
    print(f'valor de r: {r}')
    return r


def conjuncao(cl1, cl2, linhas):
    print('entrou na conjunção')
    r = []
    test(cl1, cl2)
    for c in range(linhas):
        if cl1[c] == 'V' and cl2[c] == 'V':
            r.append('V')
        else:
            r.append('F')
    cl1.clear()
    cl2.clear()
    print(f'valor de r: {r}')
    return r


def condicional(cl1, cl2, linhas):
    print('entrou no condicional')
    r = []
    test(cl1, cl2)
    for c in range(linhas):
        if cl1[c] == 'V' and cl2[c] == 'F':
            r.append('F')
        else:
            r.append('V')
    cl1.clear()
    cl2.clear()
    print(f'valor de r: {r}')
    return r


def bicondicional(cl1, cl2, linhas):
    print('entrou no bicondicional')
    r = []
    test(cl1, cl2)
    for c in range(linhas):
        if cl1[c] == 'V' and cl2[c] == 'F' or cl1[c] == 'F' and cl2[c] == 'V':
            r.append('F')
        else:
            r.append('V')
    cl1.clear()
    cl2.clear()
    print(f'valor de r: {r}')
    return r


# teste dos valores a serem calculados
def test(cl1, cl2):
    print(f'cl1 {cl1}')
    print(f'cl2 {cl2}')
