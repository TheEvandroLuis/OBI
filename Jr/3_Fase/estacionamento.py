n = int(input())
m = int(input())
planos = []
vagas = [-1 for _ in range(n+1)]
estacionados = 0

for _ in range(m):
    planos.append(int(input()))

for plano in planos:
    carro_estacionado = False
    for i in range(plano, 0, -1):
        if vagas[i]==-1:
            vagas[i]=1
            estacionados+=1
            carro_estacionado = True
            break
    if not carro_estacionado:
        break

print(estacionados)