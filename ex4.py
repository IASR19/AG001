from sympy import solve, Symbol

matr = 91
c = matr%10

def malha1(i1, i2, c):
    return 10*(i1) + (10+(2*c)) + (20*(i1-i2))

def malha2(i1, i2, c):
    return 25*(i2) + (20*(i2-i1)) + (5 + (2*c))

print('\n' * 100)

i1 = Symbol('i1')
i2 = Symbol('i2')

resultado = solve([malha1(i1, i2, c), malha2(i1, i2, c)], dict= True)
ix = -(resultado[0][i1]) # atribuindo o valor de i1 a uma variável
iy = resultado[0][i2] # atribuindo o valor de i2 a uma variável
# estrutura para o resultado vista na documentação do sympy https://docs.sympy.org/latest/modules/solvers/solvers.html

print('Resolvendo o sistema de equações temos {} '.format(resultado))

print('A corrente que passa pelo resistor de 10 ohm é de {} '.format(ix))
print('A corrente que passa pelo resistor de 25 ohm é de {} '.format(iy))
print('A corrente que passa pelo resistor de 20 ohm é de {} '.format(ix - iy))