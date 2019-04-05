"""
VALOR: 35pts

1. Ler um arquivo contendo o código genético. // até aí tá tudo tranquilo.

2. Fornecer um intervalo para os valores de K, gerando um arquivo txt para cada K (O intervalo será de 7 até 9). //  até aí ok tbm.

3. O arquivo de saída deve conter (um arquivo de saída para cada K): // 'dna_k=7.txt', 'dna_k=8.txt', 'dna_k=9.txt'
    a) As sequências que mais se repetem e sua quantidade; // falta só a quantidade, tem que fazer isso aí ainda.
    b) Quais dentre as sequências do item (a) possuem inversas e sua quantidade; // meio que já fizemos, só falta a quantidade msm.
    c) Acrescentar a taxa de mutação 'D', a qual permite uma quantidade 'D' de erros quando as comparações são feitas;// Tá, mas o que é D???

OBS: Até agora é como se tivéssemos considerado tudo como D = 0.
"""

from random import randint


"""
    Cria os 3 arquivos, passando como parâmetro o tamanho (quantidade de letras) da string
"""
def generate_txt_file(size):
    # criando arquivos de texto
    dna_k7 = open("../assets/dna_k7.txt", "a+")
    dna_k8 = open("../assets/dna_k8.txt", "a+")
    dna_k9 = open("../assets/dna_k9.txt", "a+")

    for i in range(size):
        cont = randint(1, 4)
        if cont == 1:
            char = 'A'
        elif cont == 2:
            char = 'T'
        elif cont == 3:
            char = 'C'
        else:
            char = 'G'


"""
    fatia a string no tamanho k e move ela
"""
def slice_and_switch(string, k):
    jumping = len(string) - k + 1

    for i in range(jumping):
        slice = string[i: i + k]
        create_complement(slice, string)


"""
    criando string complementar, pra depois tentar achar ela dentro da string inteira
    A string complementar é o inverso das ligações da String, por exemplo,
    o inverso da string TTGATCA é TGATCAA.
    Ou seja: seja a string (TTGATCA):
    Inverta ela (ACTAGTT);
    E substitua com as ligações de nucleotídeos (A com T, G com C e vice-versa).
"""
def create_complement(slice, string):
    complement = []

    for i in range(len(slice) - 1, -1, -1):
        switch = ''

        if slice[i] == 'a':
            switch = 't'
        elif slice[i] == 'c':
            switch = 'g'
        elif slice[i] == 'g':
            switch = 'c'
        elif slice[i] == 't':
            switch = 'a'

        complement.append(switch)
    # print("E a complementar é ", complement) por enquanto tá tudo tranquilo

    if find_string_complement(complement, string, slice):
        return True
    else:
        return False


"""
    Verifica dentro da string completa se a complementar (criada na função anterior) já existe

"""
def find_string_complement(complement, string, slice):
    flag = False

    for i in range(len(string)):
        if string[i: i + len(complement)] == complement:
            print("Primária: ", string)
            print("Secundária: ", complement)
            flag = True

    if flag:
        # print("Não vai dar não...")
        return False
    else:
        print("Primária:", slice)
        print("Complementar:", complement, "\n")
        return True


def main():
    # carregando arquivo principal e copiando para uma lista
    text_file = open("../assets/dna_vibrio_cholerae.txt", "r")
    string = text_file.readline()
    text_file.close()
    lista = []

    # ignorando a última linha, pq é uma quebra de linha (\n)
    for i in range(len(string)-1):
        lista.append(string[i:i+1])

    print(lista)

    # achando as string complementares de tamanho (7 a 9)
    print("Essas são as string complementares de tamanho 7:")
    slice_and_switch(string, 7)

if __name__ == '__main__':
    main()
