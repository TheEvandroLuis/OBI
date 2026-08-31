# Leitura padrão com input() para N (cidades) e Q (consultas)
linha_inicial = input().split()
N = int(linha_inicial[0])
Q = int(linha_inicial[1])

# Lista de adjacência para guardar a árvore de cada componente
adj = [[] for _ in range(N + 1)]

# Estruturas do DSU
pai = list(range(N + 1))
tamanho = [1] * (N + 1)
soma_pares = [0] * (N + 1)

# 1. DSU ITERATIVO COM PILHA (Sem Recursão)
def encontrar(i):
    pilha_caminho = []
    # Sobe na árvore até encontrar a raiz (onde o pai é ele mesmo)
    while pai[i] != i:
        pilha_caminho.append(i)
    i = pai[i]

    raiz = i

    # Compressão de caminho: esvazia a pilha e aponta todos diretamente para a raiz
    while pilha_caminho:
        no = pilha_caminho.pop()
    pai[no] = raiz

    return raiz

# 2. DFS ITERATIVA COM PILHA (Sem Recursão)
def soma_distancias_ate(inicio):
# A pilha guarda tuplas: (cidade_atual, distancia_acumulada_ate_aqui)
    pilha = [(inicio, 0)]
    visitados = {inicio}
    soma_dist = 0

    while pilha:
        u, d = pilha.pop()
        soma_dist += d

        for v, peso in adj[u]:
            if v not in visitados:
                visitados.add(v)
                pilha.append((v, d + peso))
            
    return soma_dist

# 3. PROCESSAMENTO DAS CONSULTAS
for _ in range(Q):
    # Lemos a linha e dividimos os itens. O primeiro indica a ação de Margaret ou da Rainha
    linha = list(map(int, input().split()))
    tipo = linha[0]

    if tipo == 1:
        # Construção de estrada: Margaret conecta A e B com tamanho D[cite: 6]
        u, v, d = linha[1], linha[2], linha[3]

        raiz_u = encontrar(u)
        raiz_v = encontrar(v)

        if raiz_u != raiz_v:
            # Calcula as distâncias usando nossa DFS iterativa com pilha
            dist_u = soma_distancias_ate(u)
            dist_v = soma_distancias_ate(v)
            
            # Matemática das novas rotas geradas
            t_u = tamanho[raiz_u]
            t_v = tamanho[raiz_v]
            soma_cruzada = (t_v * dist_u) + (t_u * t_v * d) + (t_u * dist_v)
            
            nova_soma = soma_pares[raiz_u] + soma_pares[raiz_v] + soma_cruzada
            
            # Adiciona a nova estrada ao grafo[cite: 6]
            adj[u].append((v, d))
            adj[v].append((u, d))
            
            # Une os conjuntos
            pai[raiz_v] = raiz_u
            tamanho[raiz_u] += tamanho[raiz_v]
            soma_pares[raiz_u] = nova_soma
            
    elif tipo == 2:
        # Pergunta da rainha: situação da componente contendo a cidade C[cite: 6]
        c = linha[1]
        raiz_c = encontrar(c)
        # Imprime a soma calculada
        print(soma_pares[raiz_c])