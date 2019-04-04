"""
Etapa 1 Parte 2:
-> Gerar um arquivo .txt com as K repetições;
-> Verificar as 3 opções entre as repetições;
    -> Se é igual (A - T);
    -> Se é o inverso complementar (G - C);
    -> Se não é nenhuma das opções anteriores.

"""
from random import randint


def main():
    file = list(open('../assets/dna_etapa_1_parte_2.txt', 'w+'))

    for i in range(50):
        cont = randint(1, 4)
        if cont == 1:
            char = 'A'
        elif cont == 2:
            char = 'T'
        elif cont == 3:
            char = 'C'
        else:
            char = 'G'

        file.append(char)

    print(file)


if __name__ == '__main__':
    main()
