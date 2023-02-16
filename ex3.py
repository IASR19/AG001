from sympy import Integral, Symbol

matr = 91
c = matr%10

def area(c,x):
    return ((1/x**1/3) - x**5 - 6*x - 2*c)

print('\n' * 100)

x = Symbol('x')

resultado = Integral(area(c,x), (x, 3, 6)).doit()
print('A área da curva da funçaõ (F(x)), sendo {} '.format(resultado))