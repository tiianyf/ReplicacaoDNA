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
    Cria os 3 arquivos, passando como parâmetro o tamanho (quantidade de letras)
    da string
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




def main():
    # lendo arquivo
    text_file = open("../assets/dna_vibrio_cholerae.txt", "r")
    string = text_file.readline()
    text_file.close()
    print(string)


if __name__ == '__main__':
    main()
