n = int(input())
quadrado = []
pos_i = -1
pos_j = -1
soma_magica = 0
soma_zero = 0

for i in range(n):
  linha = list(map(int, input().split()))
  soma_linha=sum(linha)
  if (soma_linha > soma_magica):
    soma_magica=soma_linha
  for j in range(n):
    if (linha[j]==0):
      pos_i = i
      pos_j = j
      soma_zero=sum(linha)
  quadrado.append(linha)

quadrado[pos_i][pos_j]= soma_magica-soma_zero

print (quadrado[pos_i][pos_j])
print (pos_i+1)
print (pos_j+1)