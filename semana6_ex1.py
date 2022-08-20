'''
Exercício 1: Soma dos elementos de uma lista

Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números 
inteiros e devolve um número inteiro correspondente à soma dos elementos desta lista.

Sua solução deve ser implementada utilizando recursão.

'''

def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    resultado = lista[0]
    resultado += soma_lista(lista[1:])
    return resultado 




# print(soma_lista([1,3,4,8,12]))
