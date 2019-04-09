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


"""
    Pegando cada sequência de tamanho k
"""
def pegar_sequencia(string, k):
    # quantas sequências de tamanho k existem na string
    numero_de_sequencias = len(string) - k + 1

    for i in range(numero_de_sequencias):
        sequencia = string[i: i + k]
        criar_string_complementar(sequencia, string)


"""
    Criando string complementar e, após isso, verificar se a mesma realmente
    existe dentro da string original.
    Lembrando que a complementar são as ligações das respectivas bases
    nitrogenadas, só que em ordem inversa.
"""
def criar_string_complementar(sequencia, string):
    complementar = ''

    # percorrer a sequência pra criar a string complementar, de trás pra frente
    for i in range(len(sequencia)-1, -1, -1):
        troca = ''
        if sequencia[i] == 'a':
            troca = 't'
        elif sequencia[i] == 'c':
            troca = 'g'
        elif sequencia[i] == 'g':
            troca = 'c'
        elif sequencia[i] == 't':
            troca = 'a'

        complementar += troca

    if buscar_string_complementar(complementar, string, sequencia):
        return True
    else:
        return False


"""
    Verifica dentro da string se a complementar (criada na função anterior)
    já existe
"""
def buscar_string_complementar(complementar, string, sequencia):
    flag = False

    # percorrendo a string pra ver se acha a complementar
    for i in range(len(string)):
        if string[i: i + len(complementar)] == complementar:
            flag = True

    if flag:
        print("Sequência: ", sequencia)
        print("Complementar: ", complementar)
        return True
    else:
        return False


def main():
    arquivo = open('../assets/dna_vibrio_cholerae.txt', 'r')
    string = arquivo.readline()
    arquivo.close()

    for i in range(7, 10):
        pegar_sequencia(string, i)


if __name__ == '__main__':
    main()
