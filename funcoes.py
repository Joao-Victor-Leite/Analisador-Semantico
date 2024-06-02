def guardar_arquivo(arquivo_caminho, arquivo_conteudo):
    with open(arquivo_caminho, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.strip()
            if linha:
                linha = ''.join(linha.split())
                arquivo_conteudo.append(linha)
    return arquivo_conteudo

def declarar_variavel_tabela(tabela_simbolos, var_nome, var_tipo, var_valor=0):
    tabela_simbolos[var_nome] = {"tipo": var_tipo, "valor": var_valor}

def atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor):
    tabela_simbolos[var_nome]["valor"] = var_valor

def procurar_variavel_em_pilha(pilha, var_nome):
    for escopo in reversed(pilha):
        if var_nome in escopo:
            return True
    return False

def procurar_valor_variavel_em_pilha(pilha, var_nome):
    for escopo in reversed(pilha):
        if isinstance(escopo, dict) and var_nome in escopo:
            return escopo[var_nome].get("valor", None)
    return None

def procurar_tipo_variavel_em_pilha(pilha, var_nome):
    for escopo in reversed(pilha):
        if isinstance(escopo, dict) and var_nome in escopo:
            return escopo[var_nome].get("tipo")
    return None

def e_numero(var):
    try:
        float(var)
        return True
    except ValueError:
        return False