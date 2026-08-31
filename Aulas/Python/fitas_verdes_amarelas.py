# OBI frequentemente testa limites de tempo, então a leitura eficiente é recomendada.
import sys

# Leitura das dimensões do mapa
N, M = map(int, sys.stdin.readline().split())

# Construção do mapa lendo os caracteres de terra ('#') e mar ('.')
mapa = [list(sys.stdin.readline().strip()) for _ in range(N)]

# Matriz auxiliar para não visitarmos o mesmo pedaço de terra duas vezes
visitado = [[False] * M for _ in range(N)]
total_fitas = 0

# Percorremos cada célula da malha[cite: 5]
for i in range(N):
    for j in range(M):
        # Se encontramos terra não visitada, achamos um novo "continente"
        if mapa[i][j] == '#' and not visitado[i][j]:
            
            continente = []
            pilha = [(i, j)]
            visitado[i][j] = True
            
            # DFS para explorar todo o continente conectado
            while pilha:
                linha_atual, coluna_atual = pilha.pop()
                continente.append((linha_atual, coluna_atual))
                
                # Olhamos os 4 vizinhos (Cima, Baixo, Esquerda, Direita)
                movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for desloc_linha, desloc_coluna in movimentos:
                    nova_linha = linha_atual + desloc_linha
                    nova_coluna = coluna_atual + desloc_coluna
                    
                    # Se o vizinho estiver dentro do mapa, for terra e não foi visitado
                    if 0 <= nova_linha < N and 0 <= nova_coluna < M:
                        if mapa[nova_linha][nova_coluna] == '#' and not visitado[nova_linha][nova_coluna]:
                            visitado[nova_linha][nova_coluna] = True
                            pilha.append((nova_linha, nova_coluna))
                            
            # Calculamos quantas fitas VERDES (horizontais) este continente precisa
            fitas_horizontais = 0
            for l, c in continente:
                # É o início de uma fita se estiver na borda esquerda ou se a célula anterior for mar
                if c == 0 or mapa[l][c-1] == '.':
                    fitas_horizontais += 1
                    
            # Calculamos quantas fitas AMARELAS (verticais) este continente precisa
            fitas_verticais = 0
            for l, c in continente:
                # É o início de uma fita se estiver na borda superior ou se a célula de cima for mar
                if l == 0 or mapa[l-1][c] == '.':
                    fitas_verticais += 1
                    
            # Adicionamos ao total o menor custo de fitas para este continente específico
            total_fitas += min(fitas_horizontais, fitas_verticais)

# Imprime a quantidade mínima total de fitas necessárias[cite: 5]
print(total_fitas)