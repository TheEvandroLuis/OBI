n, c, s =map(int,input().split())
estacoes = [0] * (n+1)
comandos = list(map(int, input().split()))
atual = 1
estacoes[atual] += 1

for comando in comandos:
  atual+= comando
  if (atual > n): 
    atual=1
  elif (atual == 0): 
    atual = n
  estacoes[atual] += 1

print(estacoes[s])