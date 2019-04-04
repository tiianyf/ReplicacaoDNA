"""
Dado uma String, verificar qual letra é a mais frequente.
"""


# criando um dicionário que armazena chave (número de repetições) e valor(a letra em questão)
def counter(string):
    count = {}
    for i in string:
        if i in string:
            count[i] += 1
        else:
            count[i] = 1

    return count


def main():
    file = open("../assets/dna_1.txt", "r")
    my_original_string = file.readline()
    file.close()
    counter(my_original_string)


if __name__ == "__main__":
    main()
