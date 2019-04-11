"""
VALOR: 35pts

1. Ler um arquivo contendo o código genético.

2. Fornecer um intervalo para os valores de K, gerando um arquivo txt para cada K (O intervalo será de 7 até 9).

3. O arquivo de saída deve conter (um arquivo de saída para cada K):
    a) As sequências que mais se repetem e sua quantidade;
    b) Quais dentre as sequências do item (a) possuem inversas e sua quantidade;
    c) Acrescentar a taxa de mutação 'D', a qual permite uma quantidade 'D' de erros quando as comparações são feitas;

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
        # criar_string_complementar(sequencia, string)
        return criar_string_complementar(sequencia, string)


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

    return buscar_string_complementar(complementar, string, sequencia)


"""
    Verifica dentro da string se a complementar (criada na função anterior)
    já existe
"""
def buscar_string_complementar(complementar, string, sequencia):
    achou = False
    # percorrendo a string pra ver se acha a complementar
    for i in range(len(string)):
        if string[i: i + len(complementar)] == complementar:
            print("Eu estive aqui")
            achou = True
            resultado = str("Sequência:" + sequencia + "\nComplementar:" + complementar )
            return resultado

    if not achou:
        return ""


def main():
    arquivo = open('../assets/dna/dna_vibrio_cholerae.txt', 'r')
    string = arquivo.readline()
    arquivo.close()

    k = int(input("\n\tInsira aqui o tamanho da string que deseja analisar: "))
    pegar_sequencia(string, k)
    # caminho = "../assets/resultados/k={}.txt".format(k)

    # arq = open(caminho, "w")
    # resultado = print(pegar_sequencia(string, k))
    # arq.write(resultado)
    # arq.close()


if __name__ == '__main__':
    main()
