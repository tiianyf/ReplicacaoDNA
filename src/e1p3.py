"""
Dado uma String, verificar qual letra é a mais frequente.
"""

# criando um dicionário que armazena chave (letra em questão) e valor(número de repetições)
# dict[chave] = valor --> dict = {'kids': 4}
# a chave 'kids' tem o valor 4 (a palavra 'kids' aparece 4 vezes)


def counter(string):
    dicionario = {}
    # varrendo tudo e armazenando em um dicionário
    for chave in string:
        if chave in dicionario.keys():
            dicionario[chave] += 1
        else:
            dicionario[chave] = 1

    return dicionario


def main():
    archive = open("../assets/dna_vibrio_cholerae.txt", "r")
    my_string = archive.readline()
    archive.close()

    print("\n\tAqui estão todas as letras e suas respectivas repetições:\n\t",
          counter(my_string))


if __name__ == "__main__":
    main()
