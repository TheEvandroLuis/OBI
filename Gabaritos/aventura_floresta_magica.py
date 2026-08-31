t = int(input())
x_atual = 0
y_atual = 0
direcao = 0 #0 = N | 90 = L | 180 = S | 270 = O

for _ in range(t):
    comando = input()
    if comando == 'M':
        passos = int(input())
        if direcao == 0: #NORTE
            y_atual+=passos #y_atual=y_atual+passos
        elif direcao == 180: #SUL
            y_atual-=passos
        elif direcao == 90: #LESTE
            x_atual+=passos
        else:
            x_atual-=passos
    if comando == 'G':
        graus = int(input())
        direcao = (direcao+graus)%360

print(f"{x_atual} {y_atual}")