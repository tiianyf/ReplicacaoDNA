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
    lista_sequencias_normais = {}
    lista_salva_complementar = open(
        "../assets/resultados/lista_de_sequencias_complementares.txt", "w")

    for i in range(numero_de_sequencias):
        sequencia = string[i: i + k]
        if sequencia in lista_sequencias_normais:
            lista_sequencias_normais[sequencia] += 1
        else:
            lista_sequencias_normais[sequencia] = 1

        criar_string_complementar(
            sequencia, string, lista_salva_complementar)

    lista_salva = open(
        '../assets/resultados/lista_de_sequencias_normais.txt', 'w')

    resultado = str(lista_sequencias_normais)
    lista_salva.write(resultado)
    lista_salva.close()
    lista_salva_complementar.close()


"""
    Criando string complementar e, após isso, verificar se a mesma realmente
    existe dentro da string original.
    Lembrando que a complementar são as ligações das respectivas bases
    nitrogenadas, só que em ordem inversa.
"""


def criar_string_complementar(sequencia, string, lista_salva_complementar):
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

    if buscar_string_complementar(complementar, string, sequencia, lista_salva_complementar):
        return True
    else:
        return False


"""
    Verifica dentro da string se a complementar (criada na função anterior)
    já existe
"""


def buscar_string_complementar(complementar, string, sequencia, lista_salva_complementar):
    achou = False

    lista_sequencias_complementares = {}
    # percorrendo a string pra ver se acha a complementar
    for i in range(len(string)):
        if string[i: i + len(complementar)] == complementar:
            if complementar in lista_sequencias_complementares:
                lista_sequencias_complementares[complementar] += 1
            else:
                lista_sequencias_complementares[complementar] = 1
            achou = True
            print("Sequência:" + sequencia + "\nComplementar:" + complementar)
            return True

    if not achou:
        return False

    resultado = str(lista_sequencias_complementares)
    resultado = eval(resultado)
    lista_salva_complementar.write(resultado)


def main():
    arquivo = open('../assets/dna/dna_vibrio_cholerae.txt', 'r')
    string = arquivo.readline()
    arquivo.close()

    k = int(input("\n\tInsira aqui o tamanho da string que deseja analisar: "))
    pegar_sequencia(string, k)


if __name__ == '__main__':
    main()
