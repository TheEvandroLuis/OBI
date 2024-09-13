n = int(input())
quadrado = []
pos_i = -1
pos_j = -1
soma_magica = 0

for _ in range(n):
  linha = list(map(int, input().split()))
  quadrado.append(linha)

for i in range(n):
  for j in range(n):
    if quadrado[i][j] == 0:
      pos_i = i
      pos_j = j

for i in range(n):
  zero = False
  soma_magica = 0
  for j in range(n):
    soma_magica += quadrado[i][j]
    if (quadrado[i][j] == 0):
      zero = True
  if (not zero):
    break

soma_linha = 0
for j in range(n):
  soma_linha += quadrado[pos_i][j]

quadrado[pos_i][pos_j] = soma_magica - soma_linha

print(quadrado[pos_i][pos_j])
print(pos_i + 1)
print(pos_j + 1)