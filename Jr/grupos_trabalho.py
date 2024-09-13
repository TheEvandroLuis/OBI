e, m, d = map(int, input().split())
amigos = []
inimigos = []
#VOU DAR UM NUMERO PARA CADA GRUPO E DEPOIS COMPARAR
grupos = [-1 for _ in range(e+1)] 
rvioladas = 0

for _ in range(m):
  x, y = map(int, input().split())
  amigos.append((x, y))

for _ in range(d):
  x, y = map(int, input().split())
  inimigos.append((x,y))

for i in range(e//3):
  a, b, c = map(int, input().split())
  grupos[a] = i
  grupos[b] = i
  grupos[c] = i

#VOU OLHAR SE OS AMIGOS ESTAO NO MESMO GRUPO
for x, y in amigos:
  if grupos[x] != grupos[y]:
    rvioladas += 1

#VOU OLHAR SE OS INIMIGOS ESTAO NO MESMO GRUPO
for x, y in inimigos:
  if grupos[x] == grupos[y]:
    rvioladas += 1

print(rvioladas)