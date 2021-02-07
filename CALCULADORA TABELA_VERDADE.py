
def tamanho4():
    a.append('V')
    a.append('V')
    a.append('F')
    a.append('F')
    b.append('V')
    b.append('F')
    b.append('V')
    b.append('F')


def tamanho8():
    a.append('V')
    a.append('V')
    a.append('V')
    a.append('V')
    a.append('F')
    a.append('F')
    a.append('F')
    a.append('F')

    b.append('V')
    b.append('V')
    b.append('F')
    b.append('F')
    b.append('V')
    b.append('V')
    b.append('F')
    b.append('F')

    c.append('V')
    c.append('F')
    c.append('V')
    c.append('F')
    c.append('V')
    c.append('F')
    c.append('V')
    c.append('F')

def tamanho16():
    a.append('V')
    a.append('V')
    a.append('V')
    a.append('V')
    a.append('V')
    a.append('V')
    a.append('V')
    a.append('V')
    a.append('F')
    a.append('F')
    a.append('F')
    a.append('F')
    a.append('F')
    a.append('F')
    a.append('F')
    a.append('F')

    b.append('V')
    b.append('V')
    b.append('V')
    b.append('V')
    b.append('F')
    b.append('F')
    b.append('F')
    b.append('F')
    b.append('V')
    b.append('V')
    b.append('V')
    b.append('V')
    b.append('F')
    b.append('F')
    b.append('F')
    b.append('F')

    c.append('V')
    c.append('V')
    c.append('F')
    c.append('F')
    c.append('V')
    c.append('V')
    c.append('F')
    c.append('F')
    c.append('V')
    c.append('V')
    c.append('F')
    c.append('F')
    c.append('V')
    c.append('V')
    c.append('F')
    c.append('F')

    d.append('V')
    d.append('F')
    d.append('V')
    d.append('F')
    d.append('V')
    d.append('F')
    d.append('V')
    d.append('F')
    d.append('V')
    d.append('F')
    d.append('V')
    d.append('F')
    d.append('V')
    d.append('F')
    d.append('V')
    d.append('F')


#LISTAS

#Proposições
a = []
b = []
c = []
d = []

#colunas
cl1 = []
cl2 = []

#auxiliares
aux = []
auxnegacao = []
aux1 = []
aux2 = []

resultado = []
r = []

# teste dos valores a serem calculados
def test(cl1, cl2):
    print(f'cl1 {cl1}')
    print(f'cl2 {cl2}')

# calculos
def disjuncao(cl1, cl2):
    print('entrou na disjunção')
    test(cl1, cl2)
    aux.clear()
    for c in range(0, linhas):
        if cl1[c] == 'F' and cl2[c] == 'F':
            r.append('F')
        else:
            r.append('V')
    cl1.clear()
    cl2.clear()
    print(f'valor de r: {r}')
    return r


def conjuncao(cl1, cl2):
    print('entrou na conjunção')
    test(cl1, cl2)
    aux.clear()
    for c in range(linhas):
        if cl1[c] == 'V' and cl2[c] == 'V':
            r.append('V')
        else:
            r.append('F')
    cl1.clear()
    cl2.clear()
    return r

def condicional(cl1, cl2):
    print('entrou no condicional')
    test(cl1, cl2)
    aux.clear()
    for c in range(linhas):
        if cl1[c] == 'V' and cl2[c] == 'F':
            r.append('F')
        else:
            r.append('V')
    cl1.clear()
    cl2.clear()
    print(f'valor de r: {r}')
    return r

def bicondicional(cl1, cl2):
    print('entrou no bicondicional')
    test(cl1, cl2)
    aux.clear()
    for c in range(linhas):
        if cl1[c] == 'V' and cl2[c] == 'F' or cl1[c] == 'F' and cl2[c] == 'V':
            r.append('F')
        else:
            r.append('V')
    cl1.clear()
    cl2.clear()
    return r

def negacao(cl1):
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


#Tabela verdade
tabela_verdade = ['a', '>', 'b', 'v', 'c']

#gambiarra
#Verifica a quantidade de proposições na tabela verdade
expoente = 0

q = tabela_verdade.count('a') + tabela_verdade.count('~a')
t = q
if t > 0:
    expoente = expoente + 1
    q = 0
    t = 0

q = tabela_verdade.count('b') + tabela_verdade.count('~b')
t = q
if t > 0:
    expoente = expoente + 1
    q = 0
    t = 0

q = tabela_verdade.count('c') + tabela_verdade.count('~c')
t = q
if t > 0:
    expoente = expoente + 1
    q = 0
    t = 0

q = tabela_verdade.count('d') + tabela_verdade.count('~d')
t = q
if t > 0:
    expoente = expoente + 1
    q = 0
    t = 0

linhas = 2 ** expoente #Quantidade de linhas é igual a: 2 potencializado a quantidade de proposições

if linhas == 4:
    tamanho4()
if linhas == 8:
    tamanho8()
if linhas == 16:
    tamanho16()

while True:
    print('--' * 20)
    print(f'Proposições restantes:{tabela_verdade}')
    print(f'Valor de resultado :  {resultado}')
    print('--' * 20)

    #Se sobrar somente o resultado ele deve parar a execução
    if len(tabela_verdade) <= 1:   #or tabela_verdade[0] == '' and tabela_verdade[1] == '':
        break

    # verificando quais as Proposições serão usadas

    # coluna 1 (cl1) ou auxiliar 1 (aux1)

    if tabela_verdade[0] == 'resultado':
        aux1 = resultado[:]
    try:
        if tabela_verdade[0] == 'a':
            aux1 = a[:]
        if tabela_verdade[0] == '~a':
            aux = a[:]
            auxnegacao = negacao(aux)
            aux.clear()
            aux1 = auxnegacao[:]
            auxnegacao.clear()
    except:
        pass

    try:
        if tabela_verdade[0] == 'b':
            aux1 = b[:]
        if tabela_verdade[0] == '~b':
            aux = b[:]
            auxnegacao = negacao(aux)
            aux.clear()
            aux1 = auxnegacao[:]
            auxnegacao.clear()
    except:
        pass

    try:
        if tabela_verdade[0] == 'c':
            aux1 = c[:]
        if tabela_verdade[0] == '~c':
            aux = c[:]
            auxnegacao = negacao(aux)
            aux.clear()
            aux1 = auxnegacao[:]
            auxnegacao.clear()
    except:
        pass

    try:
        if tabela_verdade[0] == 'd':
            aux1 = d[:]
        if tabela_verdade[0] == '~d':
            aux = d[:]
            auxnegacao = negacao(aux)
            aux.clear()
            aux1 = auxnegacao[:]
            auxnegacao.clear()
    except:
        pass

     #coluna 2 (cl2) ou auxiliar 2 (aux2)

    try:
        if tabela_verdade[2] == 'a':
            aux2 = a[:]
        if tabela_verdade[2] == '~a':
            aux = a[:]
            auxnegacao = negacao(aux)
            aux.clear()
            aux2 = auxnegacao[:]
            auxnegacao.clear()
    except:
        pass

    try:
        if tabela_verdade[2] == 'b':
            aux2 = b[:]
        if tabela_verdade[2] == '~b':
            aux = b[:]
            auxnegacao = negacao(aux)
            aux.clear()
            aux2 = auxnegacao[:]
            auxnegacao.clear()
    except:
        pass

    try:
        if tabela_verdade[2] == 'c':
            aux2 = c[:]
        if tabela_verdade[2] == '~c':
            aux = c[:]
            auxnegacao = negacao(aux)
            aux.clear()
            aux2 = auxnegacao[:]
            auxnegacao.clear()
    except:
        pass

    try:
        if tabela_verdade[2] == 'd':
            aux2 = d[:]
        if tabela_verdade[2] == '~d':
            aux = d[:]
            auxnegacao = negacao(aux)
            aux.clear()
            aux2 = auxnegacao[:]
            auxnegacao.clear()
    except:
        pass

    # verificando qual calculo sera realizado

    while True:
        #disjunção
        try:
            if tabela_verdade[1] == 'v':
                aux = disjuncao(aux1, aux2)
                resultado = aux[:]
                aux.clear
                apague()
                break
        except:
            pass

        #conjunção
        try:
            if tabela_verdade[1] == '^':
                aux = conjuncao(aux1, aux2)
                resultado = aux[:]
                aux.clear
                apague()
                break
        except:
            pass

        #condicional
        try:
            if tabela_verdade[1] == '>':
                aux = condicional(aux1, aux2)
                resultado = aux[:]
                aux.clear
                apague()
                break
        except:
            pass

        #bicondicional
        try:
            if tabela_verdade[1] == '<>':
                aux = bicondicional(aux1, aux2)
                resultado = aux[:]
                aux.clear
                apague()
                break
        except:
            pass

    #Apagar os auxiliares pois outras Proposições serão usadas
    aux1.clear()
    aux2.clear()


print('--' * 20)
print(f'\nresultado final: \n{resultado} \n')

if 'F' not in resultado:
    print('O resultado da tabela verdade é uma TAUTOLOGIA')
elif 'V' not in resultado:
    print('O resultado da tabela verdade é uma CONTRADIÇÃO')
else:
    print('O resultado da tabela verdade é uma CONTINGÊNCIA')
print('--' * 20)