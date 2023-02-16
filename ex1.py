from sympy import Limit, Symbol, S

# NUMERO DA MATRICULA e CÁLCULO DO VALOR c
#matr = int(input('Informe o número da matrícula '))
matr = 91
c = matr%10

def limite(c,x):
    return (((2*x**4)-2) / (5-(5*x**2))) * (c+4)

print('\n' * 100)

x = Symbol('x')

resultado = Limit(limite(c,x), x,0).doit()
print('O limite da função para x -> 0 é {}'.format(resultado))

resultado = Limit(limite(c,x), x, S.Infinity).doit()
print('O limite da função para x -> oo é {}'.format(resultado))

resultado = Limit(limite(c,x), x, -S.Infinity).doit()
print('O limite da função para x -> -oo é {}'.format(resultado))

# se fosse deixar o resultado salvo na variável:
# resultado1 = Limit(limite(c,x), x, 0).doit()
# resultado2 = Limit(limite(c,x), x, S.Infinity).doit()
# resutaldo2 = Limit(limite(c,x), x, -S.Infinity).doit()

# print('O limite da função para x -> 0 é {}'.format(resultado1))
# print('O limite da função para x -> oo é {}'.format(resultado2))
# print('O limite da função para x -> -oo é {}'.format(resultado3))