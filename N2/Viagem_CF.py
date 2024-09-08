def bfs(grafo, no_inicial, no_destino):
    visitado = [0] * len(grafo)
    fila = []
    pai = [-1] * (len(grafo)+1)

    visitado[no_inicial] = 1
    fila.append(no_inicial)

    while fila:
        no_atual = fila.pop(0)

        if no_atual == no_destino:
            caminho = []
            while no_atual != -1:
                caminho.append(no_atual)
                no_atual = pai[no_atual]
            return caminho[::-1] 
        
        for i in range(1, len(grafo)):
            if grafo[no_atual][i] == 1 and visitado[i] == 0 :
                visitado[i] = 1
                fila.append(i)
                pai[i] = no_atual

    return "Sem Caminho"
    
n, k = map(int, input().split())
cidades = []
mercados = [[0]]
frutas_compradas = []

#CRIA O GRAFO COM 0
for _ in range(n+1):
  cidades.append([0]*(n+1))

#PREENCHE O GRAFO
for _ in range(n-1):
  x, y = map(int, input().split())
  cidades[x][y] = 1
  cidades[y][x] = 1

#MATRIZ COM AS FRUTAS POR CIDADE
for _ in range (n):
  linha = list(map(int, input().split()))
  mercados.append(linha)

n_viagens = int(input())

for _ in range(n_viagens):
    origem, destino = map(int, input().split())
    caminho = bfs(cidades, origem, destino)

    frutas_no_caminho = [0]*k
    for cidade in caminho:
        for i in range (k):
            frutas_no_caminho[i] += mercados[cidade][i]

    frutas_compradas_no_caminho = 0
    for fruta in frutas_no_caminho:
        if fruta%2==1:
            frutas_compradas_no_caminho+=1
    frutas_compradas.append(frutas_compradas_no_caminho)      

for fruta in frutas_compradas:
    print(fruta)