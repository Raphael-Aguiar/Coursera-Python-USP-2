'''
Exercício 3: Elefantes
Este exercício tem duas partes:

Implemente a função incomodam(n) que devolve uma string contendo "incomodam " 
(a palavra seguida de um espaço) n vezes. Se n não for um inteiro estritamente 
positivo, a função deve devolver uma string vazia. Essa função deve ser 
implementada utilizando recursão.

Utilizando a função acima, implemente a função elefantes(n) que devolve uma string 
contendo a letra da música "Um elefante incomoda muita gente" de 1 até n elefantes. 
Se n não for maior que 1, a função deve devolver uma string vazia. 
Essa função também deve ser implementada utilizando recursão.

Observe que, para um elefante, você deve escrever por extenso e no singular 
("Um elefante..."); para os demais, utilize números e o plural ("2 elefantes...").

Dica: lembre-se que é possível juntar strings com o operador "+". Lembre-se também 
que é possível transformar números em strings com a função str().

Dica: Será que neste caso a base da recursão é diferente de  n == 1?

No exemplo de execução abaixo, note que há uma diferença entre como a string é e 
como ela é interpretada. Na função print o símbolo "\n" é interpretado como quebra
de linha

>>> elefantes(4)
"Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes
incomodam muita gente\n3 elefantes incomodam incomodam incomodam muito mais\n3 elefantes
incomodam muita gente\n4 elefantes incomodam incomodam incomodam incomodam muito mais"

>>> print(elefantes(4))
Um elefante incomoda muita gente
2 elefantes incomodam incomodam muito mais
2 elefantes incomodam muita gente
3 elefantes incomodam incomodam incomodam muito mais
3 elefantes incomodam muita gente
4 elefantes incomodam incomodam incomodam incomodam muito mais
>>> 
'''
def incomodam(n):
    x = 'incomodam '
    if n < 1:
        return ''
    elif n == 1:
        return x
    else:
        return x + incomodam(n-1)

def elefantes(n):
    a = 'Um elefante incomoda muita gente'
    b = a + '\n2 elefantes ' + incomodam(n) + 'muito mais\n'
    if n < 1:
        return ''
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        return elefantes(n - 1) + str(n - 1) + ' elefantes incomodam muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + "muito mais\n" 
        

# print(elefantes(7))


