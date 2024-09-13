def bfs (lago, n, m, inicio, destino):
    visitados = [[False for i in range(m+1)] for _ in range(n+1)]
    fila = []

    fila.append(inicio)
    
    

    while fila:
        x_atual, y_atual = fila.pop(0)

        if x_atual == destino[0] and y_atual == destino[1]:
            print("S")
            return

        if visitados[x_atual][y_atual] == False:
            visitados[x_atual][y_atual] == True

        for passo in range(1,4):
            if x_atual+passo <=n and lago[x_atual+passo][y_atual]:
                fila.append((x_atual+passo, y_atual))
            if x_atual-passo > 0 and lago[x_atual-passo][y_atual]:
                fila.append((x_atual-passo, y_atual))
            if y_atual+passo <=m and lago[x_atual][y_atual+passo]:
                fila.append((x_atual, y_atual+passo))
            if y_atual-passo > 0 and lago[x_atual][y_atual-passo]:
                fila.append((x_atual, y_atual-passo))
    
    print("N")

n, m = map(int, input().split())
p = int(input())
lago = [[False for i in range(m+1)] for _ in range(n+1)]

for _ in range(p):
    x, y = map(int, input().split())
    lago[x][y] = True

x_sapo, y_sapo = map(int, input().split())
x_namorada, y_namorada = map(int, input().split())

bfs(lago, n, m, (x_sapo, y_sapo), (x_namorada, y_namorada))