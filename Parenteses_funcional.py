import calculadora as ct

def adiciona_matriz():
    r = []
    r.append('M')

    r.append(contador)
    print(type(r))
    print(r)

    r = str(r)

    print(type(r))
    r = r.replace('[', '')
    r = r.replace(']', '')
    r = r.replace("'", '')
    r = r.replace(',', '')
    r = r.replace(' ', '')
    return r


#lista_principal = ['(', '(', 'a', '>', 'b', ')', '^', '(', 'a', 'v', 'c', ')', ')']
lista_principal = ['(', 'a', '>', 'b', '(', 'a', 'v', 'c', ')', ')']
# lista_principal = ['a', '>', 'b', '(', 'a', ')'] # esta com problema
# lista_principal = ['a', '>', 'b', '^', '(', 'a', 'v', 'c', ')', '>', '(', 'a', '^' 'b', ')']
# lista_principal = ['a', '>', 'b', 'v', '(', 'a', '>', 'c', ')']
l2 = lista_principal[:]
l3 = []
matriz = []
lista_entre_parenteses = []
l3 = l2[:]

laux = []
laux2 = []

inicial = 0
final = 0
contador = 0
contadori = 0
contadorf = 0

rodou = 1
while True:
    if '(' in l2:
        if '(' in l3:
            print('\n' + '* *' * 20, '\n')
            print(f'Rodou:{rodou}° - ' * 7)
            rodou = rodou + 1
            print(f'L2: {l2}')
            print(f'L3: {l3}')

            lista_entre_parenteses.clear()

            qtdD = 0
            qtdE = 0
            PosicaoE = 0
            PosicaoD = 0

            # achando parenteses
            print('==' * 20)
            print('1° verificação de posição')
            for c in range(0, len(l3)):
                if l3[c] == ')':
                    qtdD = qtdD + 1
                    if qtdE == qtdD:
                        PosicaoD = c
                        break
                if l3[c] == '(':
                    if qtdE == 0:
                        PosicaoE = c
                        qtdE = qtdE + 1
                    else:
                        qtdE = qtdE + 1

            print(f'posição esquerda: {PosicaoE}')
            print(f'quantidade esquerda: {qtdE}')
            print(f'posição direita: {PosicaoD}')
            print(f'quantidade direita: {qtdD}')
            print('==' * 20)
            for c in range(PosicaoE + 0, PosicaoD + 1):
                lista_entre_parenteses.append(l3[c])

            # segunda verificação de parenteses
            print('>>' * 20)
            print('2° verificação de posição')
            qtdD = 0
            qtdE = 0
            PosicaoEAux = 0
            PosicaoDAux = 0

            for c in range(0, len(lista_entre_parenteses)):
                if lista_entre_parenteses[c] == ')':
                    qtdD = qtdD + 1
                    if qtdE == qtdD:
                        PosicaoDAux = c
                        break
                if lista_entre_parenteses[c] == '(':
                    if qtdE == 0:
                        PosicaoEAux = c
                        qtdE = qtdE + 1
                    else:
                        qtdE = qtdE + 1

            print(f'posição esquerda: {PosicaoEAux}')
            print(f'quantidade esquerda: {qtdE}')
            print(f'posição direita: {PosicaoDAux}')
            print(f'quantidade direita: {qtdD}')
            print('>>' * 20)

            print(f'Lista auxiliar antes do pop: {lista_entre_parenteses}')
            lista_entre_parenteses.pop(PosicaoDAux)
            lista_entre_parenteses.pop(PosicaoEAux)

            l3.clear()
            l3 = lista_entre_parenteses[:]
            print(f'Lista axuliar depois do pop: {l3}')

        else:
            # Resolução do calculo e retirada do valor entre parenteses
            print()
            print('++' * 20)
            print(f'L2 na retirada de parenteses:\n{l2}')
            print(f'L3 na retirada de parenteses:\n{l3}')
            lista_entre_parenteses.clear()

            m = ct.calculadora(laux, matriz)
            matriz.append(m)

            # fazendo a variavel laux receber os valores que estão entre parenteses
            for c in range(0, len(l3)):
                laux.append(l3[c])

            # adicionando os parenteses a variavel laux, para depois comparar a tabela principal
            laux.insert(0, '(')
            laux.insert(len(laux), ')')
            print(f'laux: {laux}')

            # Condições para parar a execução

            # Se os unicos parenteses que restaram são os do inicio e fim da tabela verdade
            if laux == l2:
                print('os tamanhos são iguais')
                l2.pop()
                l2.pop(0)
                break

            # if len(laux) == 3:
            #    break

            # Andando de 1 em 1 na lista_principal(l2), procurando onde esse valor entre parenteses acontece
            final = len(laux)
            print(f'l2 antes de retirar os parenteses:\n{l2}')
            while True:
                for c in range(inicial, final):
                    laux2.append(l2[c])
                # print(f'laux2: {laux2}')

                if laux2 == laux:
                    print(f'laux2: {laux2}')
                    contadori = inicial
                    contadorf = final
                    contadorf = contadorf - 1
                    valor = contadorf - contadori
                    print(f'contadori: {contadori}')
                    print(f'contadorf: {contadorf}')
                    print(f'valor: {valor}')

                    # adiciona a resolução dos parenteses
                    l2.insert(contadori, adiciona_matriz())
                    contador = contador + 1
                    print(f'l2: {l2}')

                    # apagando os valores entre parenteses apos terem sidos resolvidos
                    for c in range(0, valor + 1):
                        l2.pop(contadori + 1)

                    l3 = l2[:]
                    laux.clear()
                    inicial = 0
                    final = 0
                    contadori = 0
                    contadorf = 0
                    print(f'l2 no while depois de retirar os parenteses:\n{l2}')
                    break
                else:
                    laux2.clear()
                    # contador = contador + 1
                    inicial = inicial + 1
                    final = final + 1
    else:
        # Ele nunca deve entrar no else, essa parte é para controle do código
        print('entrou no else')
        break

lista_principal.clear()
lista_principal = l2[:]
print('\nfim do programa')
print(lista_principal)
