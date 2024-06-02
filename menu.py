import os

def menu(diretorio):
    arquivos = os.listdir(diretorio)

    arquivos_txt = sorted([arquivo for arquivo in arquivos if arquivo.endswith('.txt')])

    # Imprimir o menu
    print("Arquivos disponíveis:")
    for i, arquivo in enumerate(arquivos_txt, start=1):
        print(f"{i}. {arquivo}")

    escolha = input("Digite o número do arquivo que deseja abrir: ")

    if escolha.isdigit() and 1 <= int(escolha) <= len(arquivos_txt):
        arquivo_escolhido = arquivos_txt[int(escolha)-1]
        caminho_completo = os.path.join(diretorio, arquivo_escolhido)
        return caminho_completo
    else:
        print("Escolha inválida. Por favor, digite um número válido.")
        return None