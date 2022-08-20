'''
Exercício 2: Encontrando ímpares em uma lista
Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista de 
números inteiros e devolve uma outra lista apenas com os números ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.
'''

def encontra_impares(lista):
    resultado = []
    if len(lista) == 1:
        if lista[0] % 2 != 0:
            resultado.append(lista[0])
        return resultado
    else:
        if lista[0] % 2 != 0:
            resultado.append(lista[0])
        resultado.extend(encontra_impares(lista[1:]))
        return resultado 

#lista = [0,1,2,3,4,5,6,7,8,9,10]
#print(encontra_impares(lista))