# Tabela_Verdade

Calculadora de Tabela verdade em Python

O código aceita até 4 proposições por enquanto.

Para alterar as proposições e operadores lógicos ir para a linha: 214

Instruções de uso:

Proposições: a, b, c, d. todas em minúsculo.

Use as proposições em ordem! 

Use os operadores lógicos: 

Disjunção: ‘v’ – minúsculo

Conjunção: ’^’

Condicional:  ‘>’

Bicondicional: ‘<>’ 

Para usar a negação use o '~'(til) antes da proposição, EX:  '~a'

exemplos de modelo:

tabela_verdade = ['a', '^', 'b']

tabela_verdade = ['a', '^', 'b', '>', '~a]

tabela_verdade = ['a', '>', 'b', 'v', 'c']

tabela_verdade = ['a', 'v', 'b', '^', 'c']

tabela_verdade = ['a', '^', 'b', '<>', 'c']

tabela_verdade = ['a', '^', 'b', '>', 'c', 'v', '~a']

- O código ainda precisa ser modularizado

- Estou aprimorando o código para aceitar tabela verdade que contenha parênteses

- Futuramente migrar o código para uma aplicação desktop ou mobile

