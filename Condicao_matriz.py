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


matriz = [['v', 'v', 'f', 'f'], ['v', 'v', 'v', 'v'], ['v', 'f', 'v', 'f']]

indice_matriz = 0
r = []
aux1 = []
aux = []
tabela_verdade = ['M1', '>', 'M2', 'v']

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
