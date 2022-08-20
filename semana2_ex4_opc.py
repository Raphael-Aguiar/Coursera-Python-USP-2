'''
Ordem lexicográfica
Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista) que
recebe uma lista de strings como parâmetro e devolve o primeiro string na ordem
lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.

Dica: revise a segunda vídeo-aula desta semana.

primeiro_lex(['oĺá', 'A', 'a', 'casa'])
# deve devolver 'A'

primeiro_lex(['AAAAAA', 'b'])
# deve devolver 'AAAAAA'

'''

def primeiro_lex(lista):
    recebe_ord = []
    temp = 0
    posicao = 0
    for i in lista: # Junta todos os ORD em uma lista chamada recebe_ord
        temp = ord(i[0])
        recebe_ord.append(temp)
    minima = min(recebe_ord) # Cria variável com o menor valor ord referente à lista
    #prova = recebe_ord.count(minima) #Cria variável prova para checar se há mais de um valor mínimo igual.
    posicao = recebe_ord.index(minima)
    posicao = lista[posicao]
    return posicao

'''

print(primeiro_lex(['Fabiana', 'Fabrícia', "Paulo", 'Sílvia', 'Raphael']))
# deve devolver 'A'

print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))
# deve devolver 'A'

print(primeiro_lex(['AAAAAA', 'b']))
# deve devolver 'AAAAAA'

'''
