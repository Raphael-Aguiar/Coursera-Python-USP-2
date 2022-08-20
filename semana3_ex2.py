# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 12:26:49 2021

Tipos de triângulos
Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado() que
devolve uma string dizendo se o triângulo é:

isósceles (dois lados iguais)

equilátero (todos os lados iguais)

escaleno (todos os lados diferentes)

Note que se o triângulo for equilátero, a função não deve devolver isósceles.

Exemplos:

t = Triangulo(4, 4, 4)
t.tipo_lado()
# deve devolver 'equilátero'

u = Triangulo(3, 4, 5)
t.tipo_lado()
# deve devolver 'escaleno'

@author: Raphael Aguiar
"""

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimetro(self):
        per = self.a + self.b + self.c
        return per
    def tipo_lado(self):
        resultado = ""
        if self.a != self.b and self.a != self.c and self.b != self.c:
            resultado = "escaleno"
        elif self.a == self.b == self.c:
            resultado = "equilátero"
        else:
            resultado = "isósceles"
        return resultado

    '''
    Triângulos retângulos
    Escreva, na classe Triangulo, o método retangulo() que devolve True se o
    triângulo for retângulo, e False caso contrário.
    '''
    def retangulo(self):
        a = int(self.a)
        b = int(self.b)
        c = int(self.c)
        hipotenusa = max(a,b,c)
        if hipotenusa == a:
            cateto1 = b
            cateto2 = c
        elif hipotenusa == b:
            cateto1 = a
            cateto2 = c
        else:
            cateto1 = a
            cateto2 = b

        if hipotenusa ** 2 == (cateto1 ** 2) + (cateto2 ** 2):
            return True
        else:
            return False
    '''
    Triângulos semelhantes

    Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe
    um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é
    semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve
    devolver True. Caso negativo, deve devolver False

    Um triângulo é semelhante a outro triângulo se a razão (divisão) entre os
    comprimentos dos seus lados forem iguais.

    Dica: você pode colocar os lados de cada um dos triângulos em uma lista
    diferente e ordená-las.

    Exemplo:

    t1 = Triangulo(2, 3, 5)
    t2 = Triangulo(4, 6, 10)
    t1.semelhantes(t2)
    # deve devolver True
    '''
    def semelhantes(self,t):
        a1 = int(self.a)
        b1 = int(self.b)
        c1 = int(self.c)
        a2 = int(t.a)
        b2 = int(t.b)
        c2 = int(t.c)
        if a1/a2 == b1/b2 == c1/c2:
            return True
        else:
            return False


'''
t1 = Triangulo(2, 3, 5)
t2 = Triangulo(4, 6, 10)
print(t1.semelhantes(t2))

t1 = Triangulo(2, 6, 7)
t2 = Triangulo(3, 4, 2)
print(t1.semelhantes(t2))

t_eq = Triangulo(7,7,7)
t_is = Triangulo (8,4,8)
t_esc = Triangulo(7,5,6)

print(t_eq.tipo_lado())
print(t_is.tipo_lado())
print(t_esc.tipo_lado())

t_ret = Triangulo(15,17,8)
t_is = Triangulo (8,4,8)
print(t_ret.retangulo())
print(t_is.retangulo())

'''