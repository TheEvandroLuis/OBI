l, c = map(int, input().split())
p = int(input())
tabuleiro = [[-1 for _ in range(c+1)] for _ in range(l+1)]

for _ in range(p):
    x, y = map(int, input().split())
    tabuleiro[x][y] = 0

for linha in tabuleiro:
    for casa in linha:
        print(casa, end=" ")
    print()