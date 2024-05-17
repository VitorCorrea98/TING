import sys


def txt_importer(path_file: str):
    txt = path_file.endswith("txt")
    if not txt:
        return sys.stderr.writelines("Formato inválido")
    try:
        with open(path_file) as file:
            file_data = file.read()
            file_data_lines = file_data.split("\n")
            return file_data_lines
    except FileNotFoundError:
        return sys.stderr.writelines(f"Arquivo {path_file} não encontrado\n")
