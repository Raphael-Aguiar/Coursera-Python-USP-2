'''
Contando vogais ou consoantes
Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro parâmetro uma string contendo uma frase e como segundo parâmetro uma outra string.
Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero de vogais presentes na frase. Quando ele for definido como "consoantes",
a função deve devolver o número de consoantes presentes na frase. Se este parâmetro não for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.

Ex:

conta_letras('programamos em python')
# deve devolver 6

conta_letras('programamos em python', 'vogais')
# deve devolver 6

conta_letras('programamos em python', 'consoantes')
# deve devolver 13

'''

def conta_letras(frase, contar="vogais"):

    descarte = " .,:;?!/0123456789"
    for i in descarte:
        frase = frase.replace(i,"")
        frase = frase.replace(" ","")
    frase = frase.upper()
    resultado = 0

    if contar == "vogais":
        descarte = "BCDFGHJKLMNPQRSTVXWYZ"

    elif contar == "consoantes":
        descarte = "AEIOU"

    for i in descarte:
        frase = frase.replace(i,"")
    resultado = len(frase)
    return resultado


def main():
    print(conta_letras('programamos em python'))
    # deve devolver 6

    print(conta_letras('programamos em python', 'vogais'))
    # deve devolver 6

    print(conta_letras('programamos em python', 'consoantes'))
    # deve devolver 13

main()