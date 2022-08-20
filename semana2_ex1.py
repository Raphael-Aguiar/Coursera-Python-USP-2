'''
Letras maiúsculas

Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.

Para resolver este exercício, pode ser útil verificar uma tabela ASCII, que contém os valores de cada caractere. Ver https://pt.wikipedia.org/wiki/ASCII

Note que para simplificar a solução do exercício, as frases passadas para a sua função não possuirão caracteres que não estejam presentes na tabela ASCII apresentada, como ç, á, É, ã, etc.

Dica: Os valores apresentados na tabela são os mesmos devolvidos pela função ord apresentada nas aulas.

Ex:

maiusculas('Programamos em python 2?')
# deve devolver 'P'

maiusculas('Programamos em Python 3.')
# deve devolver 'PP'

maiusculas('PrOgRaMaMoS em python!')
# deve devolver 'PORMMS'
 

'''

def maiusculas(frase):
    resultado = ""
    frase = frase.strip(".,:;?!/0123456789")
    frase = frase.replace(" ","")
    frase_maiuscula = frase.upper()
    i = 0
    while i < len(frase):
        if frase[i] == frase_maiuscula[i]:
            resultado = resultado + frase[i]
        i += 1
    resultado = resultado.strip(" .,:;?!/0123456789")
    resultado = resultado.replace(" ","")
    return resultado



def main():

    print(maiusculas('Programamos em python 2?'))
    # deve devolver 'P'

    print(maiusculas('Programamos em Python 3.'))
    # deve devolver 'PP'

    print(maiusculas('PrOgRaMaMoS em python!'))
    # deve devolver 'PORMMS'

    print(maiusculas('oi, Daniela e David'))
    

main()




'''
    string = []
    resultado = ""
    frase = frase.strip()
    frase_maiuscula = frase.upper()
    i = 0
    while i < len(frase):
        if frase[i] == frase_maiuscula[i] and frase[i] != "" and frase[i] != " " and frase[i] != "." and frase[i] != "," and frase[i] != "?" and frase[i] != "!" and frase[i] != "0" and frase[i] != "2":
            string.append(frase[i])
            frase = frase.strip()
        i += 1
    for j in string:
        if j == " " or  j == " " or j == "." or j == "," or j == "!" or j == "?" or j == "1" or j == "2" or j == "3" or j == "4" or j == "5" or j == "6" or j == "7" or j == "8" or j == "9": 
            string.remove(j)
    return str(string)
'''

