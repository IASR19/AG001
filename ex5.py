import math
from math import cos

from sympy import solve, Symbol, cos

matr = 91
c = matr%10

def equacao1(x,c):
    return (2.7182**x-2) + (2.7182**x-4) + (2.7182**x) - (5*(c+1))

def equacao2(x,c):
    return ((3 * (x**3)) - (2 * (x**2)) - (5*x) - (4*c))

def equacao3(x,c):
    return (2 * (cos(4*(c+1)*x)) - 5)

print('\n' * 100)

x = Symbol('x')

resultado = solve(equacao1(x,c))
print('Resultado da equação (e**x-2) + (e**x-4) + (e**x) - (5*(c+1)) = 0 é {} '.format(resultado))

resultado = solve(equacao2(x,c))
print('Resultado da equação (3*(x**3) - 2 * (x**2) - 5*x - 4*c) = 0 é {} '.format(resultado))

resultado = solve(equacao3(x,c))
print('Resultado da equação (2 * (cos(4*(c+1)*x)) - 5) = 0 é {} '.format(resultado))