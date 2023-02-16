from sympy import Integral, Derivative, Symbol

# NUMERO DA MATRICULA e CÁLCULO DO VALOR c
# matr = int(input('Informe o número da matrícula '))
matr = 91
c = matr%10

def posicao(c,t):
    return  ((t**(1/4)) + (1/t*t) - 3 * c)

def velocidade(c,t):
    return  (0.25/t**0.75)

print('\n' * 100)

t = Symbol('t')

resultado = Derivative(posicao(c,t), t).doit()
print('A velocidade é dada pela derivada da posição, cujo resultado é {} '.format(resultado))
print('Velocidade: %.3f ms' % (0.25/7**0.75))

resultado = Derivative(velocidade(c,t), t).doit()
print('A aceleração é dada pela derivada da velocidade, cujo resultado é {} '.format(resultado))
print('Aceleração: %.3f ms²' % (-0.1875/2**1.75))