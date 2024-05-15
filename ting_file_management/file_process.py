from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    linhas_arquivo = txt_importer(path_file)
    qtd_linhas = len(linhas_arquivo)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": qtd_linhas,
        "linhas_do_arquivo": linhas_arquivo,
    }
    file_already_in_line = None
    for file in instance.data:
        if file["nome_do_arquivo"] == path_file:
            file_already_in_line = file
    if not file_already_in_line:
        instance.enqueue(result)

    print(result)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
