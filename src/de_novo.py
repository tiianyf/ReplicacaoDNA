"""
ler as sequencias normais que mais se repetem

ou seja, criar a funcao pegar_sequencia(), mas somente para as sequencias
normais e salvar as sequencias mais repetidas num arquivo de texto (no caso, 3
arquivos de texto, para k=7, k=8 e k=9)

ler esse arquivo, e usar as sequencias que mais se repetem (ou melhor, todas as
sequencias que tiveram o maior número de repetições)
"""

"""
    Ler as sequências normais (não complementares) de tamanho k, e salvar o
    resultado em um arquivo.
"""


def ler_sequencias(string, k):
    numero_de_sequencias = len(string) - k + 1
    dicionario = {}

    for i in range(numero_de_sequencias):
        sequencia = string[i: i + k]
        if sequencia in dicionario:
            dicionario[sequencia] += 1
        else:
            dicionario[sequencia] = 1

    arquivo = open(
        "../assets/resultados/sequencias_k={}.txt".format(k), "w")
    resultado = str(achar_maior_repeticao(
        dicionario))
    arquivo.write(resultado)
    arquivo.close()


"""
    Percorrer todo o dicionário, achar as chaves com o maior número e retornar
    um novo dicionário contendo somente as sequências com o maior número de
    repetições.
"""


def achar_maior_repeticao(dicionario):
    novo_dicionario = {}
    maior_numero = 1

    # achando qual é a maior chave (maior número de repetições)
    for seq in dicionario:
        if dicionario[seq] > maior_numero:
            maior_numero = dicionario[seq]

    # salvando somente as sequencias com a maior repeticao no novo dicionário
    for seq in dicionario:
        if dicionario[seq] == maior_numero:
            if seq not in novo_dicionario:
                novo_dicionario[seq] = maior_numero

    return novo_dicionario


"""
    Abre o arquivo com as sequências e repetições, e tranforma em dicionário de
    novo, para que o mesmo possa ser analisado a existência de inversas
    complementares com maior facilidade.
"""


def pegando_do_arquivo_pro_dicionario(string, k):
    arquivo = open("../assets/resultados/sequencias_k={}.txt".format(k), "r")
    resultado = arquivo.readline()
    arquivo.close()
    dicionario = {}

    # transformando a string em dicionário de novo
    for i in resultado:
        if resultado[i] == ":":
            sequencia = resultado[i - (k + 1): i - 1]
            repeticoes = resultado[i + 2]
            dicionario[sequencia] = repeticoes

    return dicionario


"""

"""


def possui_inversa(string, k):
    pass


def main():
    arquivo = open("../assets/dna/dna_vibrio_cholerae.txt", "r")
    string = arquivo.readline()
    arquivo.close()

    for k in range(7, 10):
        ler_sequencias(string, k)

    for k in range(7, 10):
        pegando_do_arquivo_pro_dicionario(string, k)


if __name__ == "__main__":
    main()
