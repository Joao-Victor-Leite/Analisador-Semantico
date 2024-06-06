def guardar_arquivo(arquivo_caminho, arquivo_conteudo):
    """
    Função que lê um arquivo e guarda seu conteúdo em uma lista.

    Args:
        arquivo_caminho (str): O caminho do arquivo a ser lido.
        arquivo_conteudo (list): A lista onde o conteúdo do arquivo será armazenado.

    Retorno:
        arquivo_conteudo (list): A lista com o conteúdo do arquivo.

    A função lê o arquivo especificado pelo caminho fornecido e armazena cada linha
    não vazia, após remover espaços em branco, na lista arquivo_conteudo. Em seguida,
    retorna a lista com o conteúdo do arquivo.
    """
    with open(arquivo_caminho, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.strip()
            if linha:
                linha = ''.join(linha.split())
                arquivo_conteudo.append(linha)
    return arquivo_conteudo

def declarar_variavel_tabela(tabela_simbolos, token_tipo, var_nome, var_tipo, var_valor=0):
    """
    Função responsável por declarar uma variável na tabela de símbolos.

    Args:
        tabela_simbolos (dict): Dicionário que representa a tabela de símbolos.
        var_nome (str): Nome da variável a ser declarada.
        var_tipo (str): Tipo da variável a ser declarada.
        token_tipo (str): Tipo do token da variável a ser declarada.
        var_valor (int, opcional): Valor inicial da variável. O valor padrão é 0.

    Retorno:
        Nenhum

    Exemplo de uso:
    declarar_variavel_tabela(tabela_simbolos, "x", "int", "NUMERO", 10)
    """
    tabela_simbolos[var_nome] = {"token_tipo": token_tipo, "tipo": var_tipo, "valor": var_valor}

def atribuir_valor_variavel(pilha, var_nome, var_valor):
    """
    Atribui um valor a uma variável na pilha de escopos.

    Args:
        pilha (list): A pilha de escopos contendo as tabelas de símbolos.
        var_nome (str): O nome da variável.
        var_valor (any): O valor a ser atribuído à variável.

    Retorno:
        Nenhum
    """
    for escopo in reversed(pilha):
        if isinstance(escopo, dict) and var_nome in escopo:
            escopo[var_nome]["valor"] = var_valor
            break

def procurar_variavel_em_pilha(pilha, var_nome):
    """
    Procura uma variável na pilha de escopos.

    Args:
        pilha (list): A pilha de escopos.
        var_nome (str): O nome da variável a ser procurada.

    Retorno:
        bool: True se a variável foi encontrada, False caso contrário.
    """
    for escopo in reversed(pilha):
        if isinstance(escopo, dict) and var_nome in escopo:
            return True
    print(f"ERRO: Variavel {var_nome} nao declarada")
    return False

def procurar_valor_variavel_em_pilha(pilha, var_nome):
    """
    Procura o valor de uma variável em uma pilha de escopos.

    Args:
        pilha (list): A pilha de escopos.
        var_nome (str): O nome da variável a ser procurada.

    Retorno:
        O valor da variável se encontrada, caso contrário, retorna None.
    """
    for escopo in reversed(pilha):
        if isinstance(escopo, dict) and var_nome in escopo:
            return escopo[var_nome].get("valor", None)
    return None

def procurar_tipo_variavel_em_pilha(pilha, var_nome):
    """
    Procura o tipo de uma variável na pilha de escopos.

    Args:
        pilha (list): A pilha de escopos.
        var_nome (str): O nome da variável a ser procurada.

    Retorno:
        str or None: O tipo da variável, se encontrada. None, caso contrário.
    """
    for escopo in reversed(pilha):
        if isinstance(escopo, dict) and var_nome in escopo:
            return escopo[var_nome].get("tipo")
    return None

def e_numero(var):
    """
    Verifica se uma variável é um número.

    Args:
        var (str): A variável a ser verificada.

    Retorno:
        bool: True se a variável for um número, False caso contrário.
    """
    try:
        float(var)
        return True
    except ValueError:
        return False