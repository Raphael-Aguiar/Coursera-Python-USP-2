'''
Imprimindo matrizes
Como proposto na primeira vídeo-aula da semana, escreva uma função imprime_matriz(matriz), que recebe uma matriz como parâmetro e imprime a matriz, linha por linha. 
Note que NÃO se deve imprimir espaços após o último elemento de cada linha!
Dica: lembre da primeira parte do curso, na semana 7! A função "print" em geral adiciona uma quebra de linha ao final, mas você pode controlar isso usando o argumento opcional "end"dessa forma:

>>>print("oi")
oi
>>>
>>>print("oi", end="")
oi>>>

Ex:
minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
1 2 3
4 5 6
'''

def imprime_matriz(matriz):
    lin = 0
    col = 0
    while lin < len(matriz):
        while col < len(matriz[0]) - 1:
            print(matriz[lin][col], end=" ")
            col = col + 1
        print(matriz[lin][col], end="")
        lin = lin + 1
        col = 0
        print()
    return


def main():
    minha_matriz = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 4, 5, 1, 2, 6]]
    return imprime_matriz(minha_matriz)

main()
