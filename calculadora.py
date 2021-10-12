from variaveis_ambiente import *


def tamanho4():
    global a, b
    a = ['V', 'V', 'F', 'F']
    b = ['V', 'F', 'V', 'F']


def tamanho8():
    global a, b, c
    a = ['V', 'V', 'V', 'V', 'F', 'F', 'F', 'F']
    b = ['V', 'V', 'F', 'F', 'V', 'V', 'F', 'F']
    c = ['V', 'F', 'V', 'F', 'V', 'F', 'V', 'F']


def tamanho16():
    global a, b, c, d
    a = ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
    b = ['V', 'V', 'V', 'V', 'F', 'F', 'F', 'F', 'V', 'V', 'V', 'V', 'F', 'F', 'F', 'F']
    c = ['V', 'V', 'F', 'F', 'V', 'V', 'F', 'F', 'V', 'V', 'F', 'F', 'V', 'V', 'F', 'F']
    d = ['V', 'F', 'V', 'F', 'V', 'F', 'V', 'F', 'V', 'F', 'V', 'F', 'V', 'F', 'V', 'F']


# teste dos valores a serem calculados
def test(cl1, cl2):
    print(f'cl1 {cl1}')
    print(f'cl2 {cl2}')


def arruma_matriz(lista):
    lista = str(lista)
    lista = lista.replace('[', '')
    lista = lista.replace(']', '')
    lista = lista.replace("'", '')
    lista = lista.replace(',', '')
    lista = lista.replace(' ', '')
    for c in range(0, len(lista)):
        r.append(lista[c])
    return r


# calculos
def disjuncao(cl1, cl2, linhas):
    print('entrou na disjunção')
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


def negacao(cl1, linhas):
    print('entrou na negação')
    print(cl1)
    print(f'valor de r: {r}')
    r.clear()
    for c in range(linhas):
        if cl1[c] == 'V':
            r.append('F')
        else:
            r.append('V')
    cl1.clear()
    print(f'valor de r no final: {r}')
    return r


def apague():
    for c in range(0, 3):
        tabela_verdade.pop(0)
    tabela_verdade.insert(0, 'resultado')
    r.clear()


def calculadora(tabela_verdade, matriz=[]):
    while True:
        global resultado
        print('--' * 20)
        print(f'Proposições restantes:{tabela_verdade}')
        print(f'Valor de resultado :  {resultado}')
        print('--' * 20)

        # Se sobrar somente o resultado ele deve parar a execução
        if len(tabela_verdade) <= 1:  # or tabela_verdade[0] == '' and tabela_verdade[1] == '':
            return resultado
            # break

        # verificando quais as Proposições serão usadas

        # coluna 1 (cl1) ou auxiliar 1 (aux1)

        if tabela_verdade[0] == 'resultado':
            aux1 = resultado[:]

        try:
            if tabela_verdade[0][0] == 'M':
                indice_matriz = int(tabela_verdade[0][1:])
                # aux.append(matriz[indice_matriz])
                # print(type(aux))
                aux = matriz[indice_matriz]
                # print(f'aux: {aux}')
                # print(f'len de aux: {len(aux)}')
                aux1 = arruma_matriz(aux)
                print(f'aux1: {aux1}')
                # print(f'len de aux1: {len(aux1)}')
                aux.clear()
        except:
            pass
        # ----------- A ------------
        try:
            if tabela_verdade[0] == 'a':
                aux1 = a[:]
            if tabela_verdade[0] == '~a':
                aux = a[:]
                auxnegacao = negacao(aux, linhas)
                aux.clear()
                aux1 = auxnegacao[:]
                auxnegacao.clear()
        except:
            pass
        # ----------- B ------------
        try:
            if tabela_verdade[0] == 'b':
                aux1 = b[:]
            if tabela_verdade[0] == '~b':
                aux = b[:]
                auxnegacao = negacao(aux, linhas)
                aux.clear()
                aux1 = auxnegacao[:]
                auxnegacao.clear()
        except:
            pass
        # ----------- C ------------
        try:
            if tabela_verdade[0] == 'c':
                aux1 = c[:]
            if tabela_verdade[0] == '~c':
                aux = c[:]
                auxnegacao = negacao(aux, linhas)
                aux.clear()
                aux1 = auxnegacao[:]
                auxnegacao.clear()
        except:
            pass
        # ----------- D ------------
        try:
            if tabela_verdade[0] == 'd':
                aux1 = d[:]
            if tabela_verdade[0] == '~d':
                aux = d[:]
                auxnegacao = negacao(aux, linhas)
                aux.clear()
                aux1 = auxnegacao[:]
                auxnegacao.clear()
        except:
            pass

        # coluna 2 (cl2) ou auxiliar 2 (aux2)

        try:
            if tabela_verdade[2][0] == 'M':
                indice_matriz = int(tabela_verdade[0][1:])
                # aux.append(matriz[indice_matriz])
                # print(type(aux))
                aux = matriz[indice_matriz]
                # print(f'aux: {aux}')
                # print(f'len de aux: {len(aux)}')
                aux2 = arruma_matriz(aux)
                print(f'aux2: {aux2}')
                # print(f'len de aux1: {len(aux1)}')
                aux.clear()
        except:
            pass
        # ----------- A ------------
        try:
            if tabela_verdade[2] == 'a':
                aux2 = a[:]
            if tabela_verdade[2] == '~a':
                aux = a[:]
                auxnegacao = negacao(aux, linhas)
                aux.clear()
                aux2 = auxnegacao[:]
                auxnegacao.clear()
        except:
            pass
        # ----------- B ------------
        try:
            if tabela_verdade[2] == 'b':
                aux2 = b[:]
            if tabela_verdade[2] == '~b':
                aux = b[:]
                auxnegacao = negacao(aux, linhas)
                aux.clear()
                aux2 = auxnegacao[:]
                auxnegacao.clear()
        except:
            pass
        # ----------- C ------------
        try:
            if tabela_verdade[2] == 'c':
                aux2 = c[:]
            if tabela_verdade[2] == '~c':
                aux = c[:]
                auxnegacao = negacao(aux, linhas)
                aux.clear()
                aux2 = auxnegacao[:]
                auxnegacao.clear()
        except:
            pass
        # ----------- D ------------
        try:
            if tabela_verdade[2] == 'd':
                aux2 = d[:]
            if tabela_verdade[2] == '~d':
                aux = d[:]
                auxnegacao = negacao(aux, linhas)
                aux.clear()
                aux2 = auxnegacao[:]
                auxnegacao.clear()
        except:
            pass

        # verificando qual calculo sera realizado

        while True:
            # disjunção
            try:
                if tabela_verdade[1] == 'v':
                    aux = disjuncao(aux1, aux2, linhas)
                    resultado = aux[:]
                    aux.clear()
                    apague()
                    break
            except:
                pass

            # conjunção
            try:
                if tabela_verdade[1] == '^':
                    aux = conjuncao(aux1, aux2, linhas)
                    resultado = aux[:]
                    aux.clear()
                    apague()
                    break
            except:
                pass

            # condicional
            try:
                if tabela_verdade[1] == '>':
                    aux = condicional(aux1, aux2, linhas)
                    resultado = aux[:]
                    aux.clear()
                    apague()
                    break
            except:
                pass

            # bicondicional
            try:
                if tabela_verdade[1] == '<>':
                    aux = bicondicional(aux1, aux2, linhas)
                    resultado = aux[:]
                    aux.clear()
                    apague()
                    break
            except:
                pass

        # Apagar os auxiliares pois outras Proposições serão usadas
        aux1.clear()
        aux2.clear()


if __name__ == '__main__':
    # Tabela verdade
    tabela_verdade = ['a', '^', 'b']

    # Verifica a quantidade de proposições na tabela verdade
    expoente = 0
    # ----------- A ------------
    if 'a' in tabela_verdade or '~a' in tabela_verdade:
        expoente += 1
    # ----------- B ------------
    if 'b' in tabela_verdade or '~b' in tabela_verdade:
        expoente += 1
    # ----------- C ------------
    if 'c' in tabela_verdade or '~c' in tabela_verdade:
        expoente += 1
    # ----------- D ------------
    if 'd' in tabela_verdade or '~d' in tabela_verdade:
        expoente += 1
    # Quantidade de linhas é igual a: 2 potencializado a quantidade de proposições
    linhas = 2 ** expoente
    print(expoente)

    if linhas == 4:
        tamanho4()
    if linhas == 8:
        tamanho8()
    if linhas == 16:
        tamanho16()

    if not ('(' in tabela_verdade):
        resultado_final = calculadora(tabela_verdade)
    else:
        pass

    print('--' * 20)
    print(f'\nresultado final: \n{resultado_final} \n')

    if 'F' not in resultado_final:
        print('O resultado da tabela verdade é uma: TAUTOLOGIA')
    elif 'V' not in resultado_final:
        print('O resultado da tabela verdade é uma: CONTRADIÇÃO')
    else:
        print('O resultado da tabela verdade é uma: CONTINGÊNCIA')
    print('--' * 20)
