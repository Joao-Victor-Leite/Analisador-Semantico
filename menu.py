import os

def menu(diretorio):
    """
    Exibe um menu com os arquivos disponíveis em um diretório e permite ao usuário escolher um arquivo para abrir.

    Args:
        diretorio (str): O caminho do diretório onde estão os arquivos.

    Retorno:
        str: O caminho completo do arquivo escolhido pelo usuário.
        None: Caso a escolha seja inválida.
    """
    arquivos = os.listdir(diretorio)
    arquivos_txt = sorted([arquivo for arquivo in arquivos if arquivo.endswith('.txt')])

    # Imprimir o menu
    print("\033[1;34;40mArquivos disponíveis:\033[0m")
    print("\033[1;32;40m" + "=" * 30 + "\033[0m")
    for i, arquivo in enumerate(arquivos_txt, start=1):
        print(f"\033[1;33;40m{i}. {arquivo}\033[0m")
    print("\033[1;32;40m" + "=" * 30 + "\033[0m")

    escolha = input("\033[1;34;40mDigite o número do arquivo que deseja abrir:\033[0m")

    if escolha.isdigit() and 1 <= int(escolha) <= len(arquivos_txt):
        arquivo_escolhido = arquivos_txt[int(escolha)-1]
        caminho_completo = os.path.join(diretorio, arquivo_escolhido)
        return caminho_completo
    else:
        print("Escolha inválida. Por favor, digite um número válido.")
        return None