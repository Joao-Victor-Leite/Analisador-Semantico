def armazenar_variavel(tabela_simbolos, var_nome, var_tipo, var_valor=None):
    """
    Armazena uma variável na tabela de símbolos.

    Parâmetros:
    - tabela_simbolos (dict): A tabela de símbolos onde a variável será armazenada.
    - var_nome (str): O nome da variável a ser armazenada.
    - var_tipo (str): O tipo da variável a ser armazenada.
    - var_valor (any, opcional): O valor da variável a ser armazenada. Padrão é None.

    Exemplo de uso:
    >>> tabela = {}
    >>> armazenar_variavel(tabela, "x", "int", 10)
    >>> tabela
    {'x': {'tipo': 'int', 'valor': 10}}
    """
    tabela_simbolos[var_nome] = {"tipo": var_tipo, "valor": var_valor}

def verificar_atribuicao(tabela_simbolos, var_nome, var_valor):
    """
    Verifica se uma variável recebeu uma atribuição e atualiza a tabela de símbolos.

    Parâmetros:
    - tabela_simbolos (dict): Um dicionário que representa a tabela de símbolos.
    - var_nome (str): O nome da variável a ser verificada.
    - var_valor (str): O valor atribuído à variável.

    Retorna:
    - None

    Exceções:
    - Se a variável não estiver definida no escopo, uma mensagem de erro será exibida.

    Exemplo de uso:
    >>> tabela = {"x": {"valor": None}}
    >>> verificar_atribuicao(tabela, "x", 10)
    >>> print(tabela)
    {"x": {"valor": 10}}
    """
    if var_nome in tabela_simbolos:
        tabela_simbolos[var_nome]["valor"] = var_valor
    else:
        print(f"Erro: Variável {var_nome} não definida neste escopo.")

def verificar_tipo(tabela_simbolos, var):
    """
    Verifica o tipo de uma variável na tabela de símbolos.

    Parâmetros:
    - tabela_simbolos (dict): Um dicionário que representa a tabela de símbolos, onde as chaves são os nomes das variáveis e os valores são os atributos das variáveis.
    - var (str): O nome da variável a ser verificada.

    Retorna:
    - str: O tipo da variável.

    Exemplo de uso:
    >>> tabela = {"x": {"tipo": "int"}, "y": {"tipo": "float"}}
    >>> tipo = verificar_tipo(tabela, "x")
    >>> print(tipo)
    int
    """
    if var in tabela_simbolos:
        var_tipo = tabela_simbolos[var]["tipo"]
        return var_tipo
    else:
        print(f"A variável {var} não está definida na tabela de símbolos.")
        return None

def atribuir_valor(tabela_simbolos, var_origem, var_destino):
    """
    Atribui o valor de uma variável a outra na tabela de símbolos.

    Parâmetros:
    - tabela_simbolos (dict): Um dicionário que representa a tabela de símbolos.
    - var_origem (str): O nome da variável de origem.
    - var_destino (str): O nome da variável de destino.

    Retorna:
    - None

    Se a variável de origem e a variável de destino estiverem definidas na tabela de símbolos,
    o valor da variável de origem será atribuído à variável de destino.
    Caso contrário, uma mensagem de erro será exibida.
    """
    if var_origem in tabela_simbolos and var_destino in tabela_simbolos:
        valor_var_origem = tabela_simbolos[var_origem]["valor"]
        tabela_simbolos[var_destino]["valor"] = valor_var_origem
    else:
        print("Uma ou ambas as variáveis não estão definidas na tabela de símbolos.")

def verificar_existencia(tabela_simbolos, var):
    """
    Verifica se uma variável existe na tabela de símbolos.

    Parâmetros:
    tabela_simbolos (dict): Um dicionário que representa a tabela de símbolos.
    var (str): O nome da variável a ser verificada.

    Retorna:
    bool: True se a variável existe na tabela de símbolos, False caso contrário.

    Exibe uma mensagem indicando se a variável existe ou não na tabela de símbolos.
    """
    if var in tabela_simbolos:
        print(f"A variável {var} existe na tabela de símbolos.")
        return True
    else:
        print(f"A variável {var} não existe na tabela de símbolos.")
        return False