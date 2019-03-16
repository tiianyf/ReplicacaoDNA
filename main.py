

# fatia a string no tamanho k e move ela
def slice_and_switch(original_string, k):
    numero_de_pulos = len(original_string) - k + 1

    for i in range(numero_de_pulos):
        primaria = original_string[i: i + k]

        reverse_dna(primaria, original_string)


# criando a string reversa
def reverse_dna(primaria, original_string):
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

    if busca_string_reversa(secundaria, original_string, primaria):
        return True
    else:
        return False


# faz a busca pra ver se a string "criada" na função anterior existe na string original
def busca_string_reversa(secundaria, original_string, primaria):
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
        return True


def main():
    arquivo = open('dna.txt', 'r')
    original_string = arquivo.readline()
    lista = []

    for i in range(len(original_string)):
        lista.append(original_string[i: i+1])

    print("Essas foram as strings complementares com tamanho igual a 9\n")
    slice_and_switch(lista, 9)


if __name__ == '__main__':
    main()
