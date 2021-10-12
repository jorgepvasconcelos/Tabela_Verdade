#tabela_verdade = ['R1', '>', 'R2', 'v']
matriz = []
a = []
matrizaux = []



contador = 0

a.append('R')

a.append(contador)
print(type(a))
print(a)

a = str(a)

print(type(a))
a = a.replace('[', '')
a = a.replace(']', '')
a = a.replace("'", '')
a = a.replace(',', '')
a = a.replace(' ', '')

print(len(a))

print(a)

