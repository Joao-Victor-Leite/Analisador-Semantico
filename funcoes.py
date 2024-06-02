def armazenar_variavel(tabela_simbolos, var_nome, var_tipo, var_valor=None):
    tabela_simbolos[var_nome] = {"tipo": var_tipo, "valor": var_valor}

def atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor):
    if verificar_existencia_variavel(tabela_simbolos, var_nome):
        tabela_simbolos[var_nome]["valor"] = var_valor
    else:
        print(f"Erro: Variável {var_nome} não definida neste escopo.")

def verificar_tipo_variavel(tabela_simbolos, var):
    if verificar_existencia_variavel(tabela_simbolos, var):
        var_tipo = tabela_simbolos[var]["tipo"]
        return var_tipo
    
def verificar_valor_variavel(tabela_simbolos, var):
    if verificar_existencia_variavel(tabela_simbolos, var):
        var_valor = tabela_simbolos[var]["valor"]
        return var_valor

def atribuir_valor_entre_variaveis(tabela_simbolos, var_origem, var_destino):
    if verificar_existencia_variavel(tabela_simbolos, var_origem) and verificar_existencia_variavel(tabela_simbolos, var_destino):
        tipo_var_origem = verificar_tipo_variavel(tabela_simbolos, var_origem)
        tipo_var_destino = verificar_tipo_variavel(tabela_simbolos, var_destino)
        if tipo_var_origem == tipo_var_destino:
            valor_var_origem = verificar_valor_variavel(tabela_simbolos, var_origem)
            atribuir_valor_variavel(tabela_simbolos, var_destino, valor_var_origem)
        else:
            print(f"ERRO: Tipos incompatíveis - {tipo_var_origem} e {tipo_var_destino}")

def verificar_existencia_variavel(tabela_simbolos, var):
    if var in tabela_simbolos:
        return True
    else:
        print(f"ERRO: Variável não declarada - {var}")
        return False
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
