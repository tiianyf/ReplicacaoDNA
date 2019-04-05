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
    file = (open('../assets/dna_criado_teste.txt', 'w+'))

    for i in range(100):
        cont = randint(1, 4)
        if cont == 1:
            char = 'A'
        elif cont == 2:
            char = 'T'
        elif cont == 3:
            char = 'C'
        else:
            char = 'G'

        file.write(char)
    file.close()


if __name__ == '__main__':
    main()
