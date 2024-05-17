def support_word(word, linhas, conteudo):
    ocorrencias = list()
    for index, linha in enumerate(linhas):
        for linha_word in linha.split(" "):
            if word.lower() in linha_word.lower():
                if conteudo:
                    ocorrencias.append({"linha": index + 1, "conteudo": linha})
                else:
                    ocorrencias.append({"linha": index + 1})
    return ocorrencias


def find_word(word, instance, conteudo):
    lista = instance.data
    result = list()
    for arquivo_objeto in lista:
        arquivo = arquivo_objeto["nome_do_arquivo"]
        linhas = arquivo_objeto["linhas_do_arquivo"]
        ocorrencias = support_word(word, linhas, conteudo)
        print(ocorrencias)
        if len(ocorrencias):
            result.append(
                {
                    "palavra": word,
                    "arquivo": arquivo,
                    "ocorrencias": ocorrencias,
                }
            )

    return result


def exists_word(word, instance):
    return find_word(word, instance, False)


def search_by_word(word, instance):
    return find_word(word, instance, True)
