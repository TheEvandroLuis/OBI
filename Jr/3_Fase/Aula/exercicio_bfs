def bfs(grafo, n_inicio, n_destino):
    visitados = [0] * len(grafo)
    fila = []
    pai = [-1] * len(grafo)

    fila.append(n_inicio)
    visitados[n_inicio] = 1

    while fila:
        n_atual = fila.pop(0)
        caminho=[]
        if(n_atual==n_destino):
           while n_atual != -1:
               caminho.append(n_atual)
               n_atual=pai[n_atual]           
           return caminho[::-1]
        for i in range(len(grafo)):
            if grafo[n_atual][i] == 1 and visitados[i] ==0:
                visitados[i]=1
                fila.append(i)
                pai[i]= n_atual
     
    return "Sem Caminho"

grafo = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]
inicio = 0
destino = 3
caminho = bfs(grafo, inicio, destino)
print(caminho)