"""
k-mers counting
Etapa 1 Parte 1:
-> Separar em grupos de 9 letras o arquivo;
-> Armazenar numa estrutura de dados;
-> Comparar as palavras de 9 letras;
-> Contar suas repetições.

"""

repeticoes = 0


# fatia a string no tamanho k e move ela
def slice_and_switch(original_string, k, repeticoes):
    numero_de_pulos = len(original_string) - k + 1

    for i in range(numero_de_pulos):
        primaria = original_string[i: i + k]

        reverse_dna(primaria, original_string, repeticoes)


# criando a string reversa
def reverse_dna(primaria, original_string, repeticoes):
    secundaria = []

    for i in range(len(primaria) - 1, -1, -1):
        troca = ''

        if primaria[i] == 'a':
            troca = 't'
        elif primaria[i] == 'c':
            troca = 'g'
        elif primaria[i] == 'g':
            troca = 'c'
        elif primaria[i] == 't':
            troca = 'a'

        secundaria.append(troca)

    if busca_string_reversa(secundaria, original_string, primaria, repeticoes):
        return True
    else:
        return False


# faz a busca pra ver se a string "criada" na função anterior existe na string original
def busca_string_reversa(secundaria, original_string, primaria, repeticoes):
    flag = False

    for i in range(len(original_string)):
        if original_string[i: i + len(secundaria)] == secundaria:
            # print("Primária: ", original_string)
            # print("Secundária: ", secundaria)
            flag = True

    if not flag:
        return False
    else:
        print("Primária:", primaria)
        print("Secundária:", secundaria, "\n")
        repeticoes += 1
        return True


def main():
    arquivo = open('../assets/dna_vibrio_cholerae.txt', 'r')
    original_string = arquivo.readline()
    lista = []

    for i in range(len(original_string)):
        lista.append(original_string[i: i+1])

    repeticoes = 0
    # tamanho igual a 9
    print("Essas foram as strings complementares com tamanho igual a 9\n")
    slice_and_switch(lista, 9, repeticoes)
    print("Totalizando, são ", repeticoes/2, "repetições")

    # tamanho fornecido pelo usuário
    # k = int(input("Insira aqui o tamanho da string que deseja analisar: "))
    # slice_and_switch(lista, k)

    # varrendo a string toda (demora muito)
    # for i in range(2, 20):
    #     slice_and_switch(original_string, i)


if __name__ == '__main__':
    main()
