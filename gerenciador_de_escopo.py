import funcoes as f

file_path = './tests/exemplo1.txt'
arquivo_conteudo = []
pilha = []
tabela_simbolos = {}
        
with open(file_path, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        linha = linha.strip()
        if linha:
            linha = ''.join(linha.split())
            arquivo_conteudo.append(linha)

for elemento in arquivo_conteudo:
    if elemento.startswith("BLOCO"):
        # Extrai o nome do bloco
        partes = elemento.split("_", 1)
        if len(partes) > 1:
            nome_bloco = "_" + partes[1]
            pilha.append(nome_bloco)
            tabela_simbolos = {}
            pilha.append(tabela_simbolos)

    elif elemento.startswith("FIM"):
        partes = elemento.split("_", 1)
        if len(partes) > 1:
            nome_bloco = "_" + partes[1]
            while nome_bloco in pilha:
                pilha.pop()

    elif elemento.startswith("PRINT"):
        var_nome = elemento[5:]  # Pega todos os caracteres após o quinto
        # Verifica se a variável existe na tabela de símbolos
        var_valor = f.procurar_valor_variavel_em_escopos(pilha, var_nome)
        if var_valor:
            print(var_valor)
        else:
            print(f"Erro: Variável {var_nome} não definida neste escopo.")

    elif elemento.startswith("NUMERO"):
        if "=" not in elemento:
            var_nome = elemento[6:]
            f.armazenar_variavel(tabela_simbolos, var_nome, "NUMERO")
        else:
            if "," in elemento:
                partes = elemento[6:].split(',')
                for parte in partes:
                    if '=' in parte:
                        var_nome, var_valor = parte.split('=')
                        f.armazenar_variavel(tabela_simbolos, var_nome, "NUMERO")
                        f.atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor)
            else:
                partes = elemento[6:].split('=')
                var_nome = partes[0].strip()
                var_valor = partes[1].strip()
                f.armazenar_variavel(tabela_simbolos, var_nome, "NUMERO")
                f.atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor)
        
    elif elemento.startswith("CADEIA"):
        if "=" not in elemento:
            var_nome = elemento[6:]
            f.armazenar_variavel(tabela_simbolos, var_nome, "CADEIA")
        else:
            if "," in elemento:
                partes = elemento[6:].split(',')
                for parte in partes:
                    if '=' in parte:
                        var_nome, var_valor = parte.split('=')
                        f.armazenar_variavel(tabela_simbolos, var_nome, "CADEIA")
                        f.atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor)
                    else:
                        print(f"Erro: Formato inválido para declaração de variável: {parte}")
            else:
                partes = elemento[6:].split('=')
                var_nome = partes[0].strip()
                var_valor = partes[1].strip()
                f.armazenar_variavel(tabela_simbolos, var_nome, "CADEIA")
                f.atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor)
    
    # Verifica se é uma atribuição
    elif "=" in elemento: 
        var_nome, var_valor = elemento.split('=', 1)
        if f.verificar_tipo_variavel(tabela_simbolos, var_nome) == "CADEIA" and var_valor.startswith('"') and var_valor.endswith('"'):
            f.atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor)
        elif f.verificar_tipo_variavel(tabela_simbolos, var_nome) == "NUMERO" and f.is_number(var_valor):
            f.atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor)
        else:
            f.atribuir_valor_entre_variaveis(tabela_simbolos, var_nome, var_valor)