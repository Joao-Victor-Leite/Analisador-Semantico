import funcoes as f

file_path = 'exemplo1.txt'
arquivo_conteudo = []
pilha = []
tabela_simbolos = {}
        
with open(file_path, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        linha = linha.strip()
        # Ignora linhas vazias
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
            print(f"INICIO DO BLOCO: {nome_bloco}")
            tabela_simbolos = {}
            pilha.append(tabela_simbolos)

    elif elemento.startswith("FIM"):
        partes = elemento.split("_", 1)
        if len(partes) > 1:
            nome_bloco = "_" + partes[1]
            while nome_bloco in pilha:
                a = pilha.pop()
                print(f"ITEM EXCLUIDO: {a}")
            if nome_bloco in pilha:
                print(f"FIM DO BLOCO: {nome_bloco}")

    elif elemento.startswith("PRINT"):
        var_nome = elemento[5:]  # Pega todos os caracteres após o quinto
        # Verifica se a variável existe na tabela de símbolos
        for tabela_simbolos in reversed(pilha):
            if var_nome in tabela_simbolos:
                print(tabela_simbolos[var_nome]["valor"])
                #break
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
                        f.verificar_atribuicao(tabela_simbolos, var_nome, var_valor)
                    else:
                        print(f"Erro: Formato inválido para declaração de variável: {parte}")
            else:
                partes = elemento[6:].split('=')
                var_nome = partes[0].strip()
                var_valor = partes[1].strip()

            f.verificar_atribuicao(tabela_simbolos, var_nome, var_valor)
        
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
                        f.verificar_atribuicao(tabela_simbolos, var_nome, var_valor)
                    else:
                        print(f"Erro: Formato inválido para declaração de variável: {parte}")
            else:
                partes = elemento[6:].split('=')
                var_nome = partes[0].strip()
                var_valor = partes[1].strip()

            f.verificar_atribuicao(tabela_simbolos, var_nome, var_valor)

    elif "=" in elemento:  # Atualiza o valor da variável
        partes = elemento.split('=')
        var_nome, var_valor = elemento.split('=', 1)
        if f.verificar_existencia(tabela_simbolos, var_nome):
            var_tipo = f.verificar_tipo(tabela_simbolos, var_nome)





        var_valor = var_valor.replace('"', '').strip()
        if var_nome in tabela_simbolos:
            tabela_simbolos[var_nome]["valor"] = var_valor
